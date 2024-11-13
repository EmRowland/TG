from django.shortcuts import render
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404


urlpatterns = [
    path("user/subscribe", views.subscribe, name="subscribe"),
    path("user/event/", views.subscribe_to_events, name="subscribe_event"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
