import datetime
from django.shortcuts import render
from django.http import HttpResponse

import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import HamperRequest
from .forms import HamperRequestForm

# used to display 'Hello Guest.'
USERNAME = "Guest"  

# Three views for the Home, About and Contact pages
def home(request):
    """
    Home page for Project Red – November giving campaign.
    """
    context = {
        "page_title": "Home",
        "current_year": datetime.date.today().year,
        "username": USERNAME,
    }
    return render(request, "projectRed/home.html", context)


def about(request):
    """
    About Project Red – what it is and why it runs in November.
    """
    context = {
        "page_title": "About",
        "current_year": datetime.date.today().year,
        "username": USERNAME,

        
    }
    return render(request, "projectRed/about.html", context)


def contact(request):
    """
    Contact page – how to get in touch about donations or support.
    """
    context = {
        "page_title": "Contact",
        "current_year": datetime.date.today().year,
        "username": USERNAME,
    }
    return render(request, "projectRed/contact.html", context)

def hamper_list(request):
    """
    List all hamper requests (Read).
    """
    hampers = HamperRequest.objects.order_by("-created_at")
    context = {
        "page_title": "Hamper Requests",
        "current_year": datetime.date.today().year,
        "username": USERNAME,
        "hampers": hampers,
    }
    return render(request, "projectRed/hamper_list.html", context)


def hamper_detail(request, pk):
    """
    Show a single hamper request (Read).
    """
    hamper = get_object_or_404(HamperRequest, pk=pk)
    context = {
        "page_title": f"Hamper for {hamper.student_name}",
        "current_year": datetime.date.today().year,
        "username": USERNAME,
        "hamper": hamper,
    }
    return render(request, "projectRed/hamper_detail.html", context)


def hamper_create(request):
    """
    Create a new hamper request (Create).
    """
    if request.method == "POST":
        form = HamperRequestForm(request.POST)
        if form.is_valid():
            form.save()
            # Show it on the site immediately by sending user back to the list
            return redirect("hamper_list")
    else:
        form = HamperRequestForm()

    context = {
        "page_title": "Create Hamper Request",
        "current_year": datetime.date.today().year,
        "username": USERNAME,
        "form": form,
    }
    return render(request, "projectRed/hamper_form.html", context)


def hamper_update(request, pk):
    """
    Update an existing hamper request (Update).
    """
    hamper = get_object_or_404(HamperRequest, pk=pk)

    if request.method == "POST":
        form = HamperRequestForm(request.POST, instance=hamper)
        if form.is_valid():
            form.save()
            return redirect("hamper_detail", pk=hamper.pk)
    else:
        form = HamperRequestForm(instance=hamper)

    context = {
        "page_title": f"Edit Hamper for {hamper.student_name}",
        "current_year": datetime.date.today().year,
        "username": USERNAME,
        "form": form,
        "hamper": hamper,
    }
    return render(request, "projectRed/hamper_form.html", context)


def hamper_delete(request, pk):
    """
    Delete a hamper request (Delete).
    """
    hamper = get_object_or_404(HamperRequest, pk=pk)

    if request.method == "POST":
        hamper.delete()
        return redirect("hamper_list")

    context = {
        "page_title": f"Delete Hamper for {hamper.student_name}",
        "current_year": datetime.date.today().year,
        "username": USERNAME,
        "hamper": hamper,
    }
    return render(request, "projectRed/hamper_confirm_delete.html", context)


def custom_404(request, exception):
    """
    Custom 404 page for non-existent routes.
    """
    context = {
        "page_title": "Page not found",
        "username": USERNAME,
        "current_year": datetime.date.today().year,
    }
    return render(request, "projectRed/404.html", context, status=404)