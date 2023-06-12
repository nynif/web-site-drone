from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    # path("prestations/", views.services, name="services"),
    path("realisations/", views.work, name="work"),
    path("tarifs/", views.price, name="price"),
    # path("blog/", views.blog, name="blog"),
    path("apropos/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("template/", views.template, name="template"),
]