from django.shortcuts import render, get_object_or_404
from .models import TourPackage
from destinations.models import Destination
from reviews.models import Review
from django.db.models import Avg
from bookings.models import Booking

def package_list(request):
    packages = TourPackage.objects.filter(
        is_available=True
    ).annotate(
        average_rating=Avg('reviews__rating')
    )

    context = {
        'packages': packages
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

    context = {
        'package': package,
        'reviews': reviews,'already_reviewed': already_reviewed,
        'average_rating': average_rating,
        'can_review': can_review,
        'already_reviewed': already_reviewed,
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