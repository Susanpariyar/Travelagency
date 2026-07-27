from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Wishlist
from packages.models import TourPackage
from django.http import HttpResponseRedirect


@login_required
def add_to_wishlist(request, slug):

    package = get_object_or_404(
        TourPackage,
        slug=slug
    )

    Wishlist.objects.get_or_create(
        user=request.user,
        package=package
    )

    messages.success(
        request,
        "Package added to your wishlist."
    )

    return redirect(
        'package_detail',
        slug=slug
    )


@login_required
def remove_from_wishlist(request, slug):

    package = get_object_or_404(
        TourPackage,
        slug=slug
    )

    Wishlist.objects.filter(
        user=request.user,
        package=package
    ).delete()

    messages.success(
        request,
        "Package removed from your wishlist."
    )

    return redirect(
        'my_wishlist'
    )


@login_required
def my_wishlist(request):

    wishlist_items = Wishlist.objects.filter(
        user=request.user
    )

    context = {
        "wishlist_items": wishlist_items
    }

    return render(
        request,
        "wishlist/my_wishlist.html",
        context
    )


@login_required
def toggle_wishlist(request, slug):

    package = get_object_or_404(
        TourPackage,
        slug=slug
    )

    item = Wishlist.objects.filter(
        user=request.user,
        package=package
    )

    if item.exists():

        item.delete()

        messages.success(
            request,
            "Package removed from your wishlist."
        )

    else:

        Wishlist.objects.create(
            user=request.user,
            package=package
        )

        messages.success(
            request,
            "Package added to your wishlist."
        )

    return HttpResponseRedirect(
        request.META.get(
            "HTTP_REFERER",
            "/"
        )
    )