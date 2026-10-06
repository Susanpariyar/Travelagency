from django.shortcuts import render, get_object_or_404
from .models import TourPackage
from destinations.models import Destination
from reviews.models import Review
from django.db.models import Avg
from bookings.models import Booking
from wishlist.models import Wishlist

def package_list(request):

    packages = TourPackage.objects.filter(
        is_available=True
    ).annotate(
        average_rating=Avg('reviews__rating')
    )

    # Search by package name
    search = request.GET.get('search', '')

    if search:
        packages = packages.filter(
            name__icontains=search
        )

    # Filter by destination
    destination_id = request.GET.get('destination', '')

    if destination_id:
        packages = packages.filter(
            destination_id=destination_id
        )

    # Sort by price
    sort = request.GET.get('sort', '')

    if sort == 'low':
        packages = packages.order_by('price')

    elif sort == 'high':
        packages = packages.order_by('-price')

    context = {
        'packages': packages,
        'destinations': Destination.objects.all(),
        'search': search,
        'selected_destination': destination_id,
        'selected_sort': sort,
    }

    return render(
        request,
        'packages/package_list.html',
        context
    )


def package_detail(request, slug):

    package = get_object_or_404(
        TourPackage,
        slug=slug,
        is_available=True
    )

    reviews = Review.objects.filter(
        package=package
    ).select_related('user')

    average_rating = reviews.aggregate(
        Avg('rating')
    )['rating__avg']


    
    can_review = False
    already_reviewed = False

    if request.user.is_authenticated:

        can_review = Booking.objects.filter(
            user=request.user,
            package=package,
            booking_status='Confirmed'
        ).exists()

        already_reviewed = Review.objects.filter(
            user=request.user,
            package=package
        ).exists()


    is_in_wishlist = False

    if request.user.is_authenticated:

        is_in_wishlist = Wishlist.objects.filter(
            user=request.user,
            package=package
        ).exists()


    context = {
        'package': package,
        'reviews': reviews,'already_reviewed': already_reviewed,
        'average_rating': average_rating,
        'can_review': can_review,
        'already_reviewed': already_reviewed,
        'package': package,
        'is_in_wishlist': is_in_wishlist,
    }



    return render(
        request,
        'packages/package_detail.html',
        context
    )


def destination_packages(request, slug):
    destination = get_object_or_404(
        Destination,
        slug=slug
    )

    packages = TourPackage.objects.filter(
        destination=destination,
        is_available=True
    ).annotate(
        average_rating=Avg('reviews__rating')
    )

    context = {
        'destination': destination,
        'packages': packages
    }

    return render(
        request,
        'packages/package_list.html',
        context
    )