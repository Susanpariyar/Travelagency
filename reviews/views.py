from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Review
from .forms import ReviewForm
from packages.models import TourPackage
from bookings.models import Booking


@login_required
def add_review(request, slug):

    package = get_object_or_404(
        TourPackage,
        slug=slug
    )

    booking = Booking.objects.filter(
        user=request.user,
        package=package,
        booking_status='Confirmed'
    ).exists()

    if not booking:

        messages.error(
            request,
            "You can only review packages that you have booked."
        )

        return redirect(
            'package_detail',
            slug=slug
        )



    existing_review = Review.objects.filter(
        user=request.user,
        package=package
    ).first()

    if existing_review:

        messages.warning(
            request,
            "You have already reviewed this package."
        )

        return redirect(
            'package_detail',
            slug=slug
        )

    if request.method == "POST":

        form = ReviewForm(request.POST)

        if form.is_valid():

            review = form.save(commit=False)

            review.user = request.user
            review.package = package

            review.save()

            messages.success(
                request,
                "Review submitted successfully."
            )

            return redirect(
                'package_detail',
                slug=slug
            )

    else:

        form = ReviewForm()

    context = {
        'form': form,
        'package': package,
    }

    return render(
        request,
        'reviews/add_review.html',
        context
    )