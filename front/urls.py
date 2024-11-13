"""
URL configuration for front project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500, handler403
from django.shortcuts import render


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("contact", views.contact, name="contact"),
    path("user", include("main.urls")),
    path("<slug:slug>/", views.PostDetail.as_view(), name="post_detail"),
    path("event_detail/<int:event_id>/", views.get_event, name="event_detail"),
    path("image/<int:image_id>/", views.get_image_details, name="image_details"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = "front.views.my_page_not_found"
handler500 = "front.views.my_page_maintenance"
handler403 = "front.views.my_page_forbidden"
