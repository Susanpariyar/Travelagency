from django.shortcuts import render
from destinations.models import Destination
from communications.forms import ContactMessageForm
from django.contrib import messages


def home(request):

    featured_destinations = Destination.objects.filter(
        is_featured=True
    )[:6]

    context = {
        "featured_destinations": featured_destinations
    }

    return render(
        request,
        "core/home.html",
        context
    )


def about(request):
    return render(
        request,
        "core/about.html"
    )


def contact(request):

    if request.method == "POST":

        form = ContactMessageForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Your message has been sent successfully. We will contact you soon."
            )

            form = ContactMessageForm()

    else:

        form = ContactMessageForm()

    context = {
        "form": form
    }

    return render(
        request,
        "core/contact.html",
        context
    )