from django.shortcuts import render, get_object_or_404
from .models import TourPackage
from destinations.models import Destination


def package_list(request):
    packages = TourPackage.objects.filter(
        is_available=True
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

    context = {
        'package': package
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