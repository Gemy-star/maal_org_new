from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomePageView.as_view(),name='home_page'),
    path('blogs', views.BlogsPageView.as_view(), name='blogs_page'),
    path('blog/detail/<int:pk>', views.BlogDetailPageView.as_view(), name='blog_detail_page'),
    path("submit-contact/", views.submit_contact, name="submit_contact"),
    path("contact/", views.ContactPageView.as_view(), name="contact_page"),
    path("about/", views.AboutPageView.as_view(), name="about_page"),
    path('projects/', views.project_list, name='project_list'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),

]
