from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from packages.models import TourPackage
from .models import Booking
from .forms import BookingForm


@login_required
def book_package(request, slug):

    package = get_object_or_404(
        TourPackage,
        slug=slug,
        is_available=True
    )

    if request.method == "POST":

        form = BookingForm(request.POST)

        if form.is_valid():

            booking = form.save(commit=False)

            if booking.travelers > package.available_slots:

                form.add_error(
                    "travelers",
                    f"Only {package.available_slots} slots are available."
                )

            else:

                booking.user = request.user
                booking.package = package

                booking.save()

                messages.success(
                    request,
                    "Your booking has been submitted successfully."
                )

                return redirect("my_bookings")

    else:

        form = BookingForm()

    context = {
        "package": package,
        "form": form,
    }

    return render(
        request,
        "bookings/book_package.html",
        context
    )


@login_required
def my_bookings(request):

    bookings = Booking.objects.filter(
        user=request.user
    ).order_by('-created_at')

    context = {
        "bookings": bookings
    }

    return render(
        request,
        "bookings/my_bookings.html",
        context
    )

@login_required
def booking_detail(request, booking_id):

    booking = get_object_or_404(
        Booking,
        booking_id=booking_id,
        user=request.user
    )

    context = {
        'booking': booking
    }

    return render(
        request,
        'bookings/booking_detail.html',
        context
    )




@login_required
def cancel_booking(request, booking_id):

    booking = get_object_or_404(
        Booking,
        booking_id=booking_id,
        user=request.user
    )

    if booking.booking_status != "Pending":

        messages.error(
            request,
            "Only pending bookings can be cancelled."
        )

        return redirect(
            "booking_detail",
            booking_id=booking.booking_id
        )

    if request.method == "POST":

        booking.booking_status = "Cancelled"
        booking.save()

        messages.success(
            request,
            "Your booking has been cancelled successfully."
        )

        return redirect("my_bookings")

    context = {
        "booking": booking
    }

    return render(
        request,
        "bookings/cancel_booking.html",
        context
    )
