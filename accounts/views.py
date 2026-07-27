from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

from bookings.models import Booking
from wishlist.models import Wishlist
from reviews.models import Review
from django.db.models import Sum


def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully. You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


@login_required
def dashboard(request):

    booking_count = Booking.objects.filter(
        user=request.user
    ).count()

    wishlist_count = Wishlist.objects.filter(
        user=request.user
    ).count()

    review_count = Review.objects.filter(
        user=request.user
    ).count()

    total_paid = Booking.objects.filter(
        user=request.user,
        payment_status='Paid'
    ).aggregate(
        total=Sum('total_price')
    )['total'] or 0

    context = {
        'booking_count': booking_count,
        'wishlist_count': wishlist_count,
        'review_count': review_count,
        'total_paid': total_paid,
    }

    return render(
        request,
        'accounts/dashboard.html',
        context
    )


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'accounts/edit_profile.html', context)