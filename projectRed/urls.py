from django.urls import path
from projectRed import views
from projectRed import views as project_views


urlpatterns = [
    # Home route
    path("", views.home, name="home"),

    # About Us Page route
    path("about/", views.about, name="about"),

    # Contact Us Page route
    path("contact/", views.contact, name="contact"),

    # Hamper Requests CRUD
    
    # Displays all hamper requests
    path("hampers/", views.hamper_list, name="hamper_list"),

    # Form to create a new hamper request
    path("hampers/new/", views.hamper_create, name="hamper_create"),

    # Shows details for a specific hamper request
    path("hampers/<int:pk>/", views.hamper_detail, name="hamper_detail"),

    # Form to edit an existing hamper request
    path("hampers/<int:pk>/edit/", views.hamper_update, name="hamper_update"),

    # Confirmation page to delete a hamper request
    path("hampers/<int:pk>/delete/", views.hamper_delete, name="hamper_delete"),
]

