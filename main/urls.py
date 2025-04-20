from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomePageView.as_view(),name='home_page'),
    path("submit-contact/", views.submit_contact, name="submit_contact"),

]