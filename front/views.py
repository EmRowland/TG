from typing import Any, Dict
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.contrib.messages import constants as messages
from django.template.loader import render_to_string
from django.contrib import messages
from django.views import generic
from .emails import SendAdminMail
from main.models import (
    Events,
    MahnazImages,
    Testimonies,
    FrequentQuestions,
    Post,
    OurImages,
    MahnazContacts,
)
from django.http import JsonResponse


# Create your views here.


def contact(request):
    form = Events()
    try:
        if request.method == "POST":
            subject = request.POST["subject"]
            message = request.POST["message"]
            sender = request.POST["sender"]
            # first_name = form.cleaned_data['first_name']
            full_name = request.POST["full_name"]
            # full_name = first_name + "" + last_name
            to = sender

            mail_subject = subject
            message = render_to_string(
                "email/contact.html",
                {
                    "subject": mail_subject,
                    "full_name": full_name,
                    "email": sender,
                    "message": message,
                },
            )
            to_email = to
            email = EmailMessage(mail_subject, message, to=[to_email])

            email.send()
            SendAdminMail(full_name, sender, message)
            message_s = messages.success(
                request, "Your request has being received successfully"
            )
            return redirect(request.META.get("HTTP_REFERER"))

        else:
            return redirect("home")
        # return redirect(request.META.get("HTTP_REFERER"))
    except Exception:
        return redirect("home")

    return redirect(request.META.get("HTTP_REFERER"))


def home(request):
    mahnazs = MahnazImages.objects.all().order_by("-id")[:6]
    ourimages = OurImages.objects.all().order_by("-id")[:12]
    events = Events.objects.all().order_by("-id")[:10]
    testimonies = Testimonies.objects.all()
    faqs = FrequentQuestions.objects.all()[:6]
    queryset = Post.objects.filter(status=1).order_by("-created_at")[:3]
    pic = Post.objects.filter(status=1).order_by("-created_at").all()[3:]
    contact = MahnazContacts.objects.all()

    cxt = {
        "ourimages": ourimages,
        "testimonies": testimonies,
        "faqs": faqs,
        "events": events,
        "mahnazs": mahnazs,
        "blogs": queryset,
        "contacts": contact,
    }

    return render(request, "index.html", cxt)


class PostDetail(generic.DetailView):
    queryset = Post.objects.filter(status=1).order_by("-created_at")
    pic = Post.objects.filter(status=1).order_by("-created_at").all()[3:]
    contact = MahnazContacts.objects.all()
    ctx = {
        "blogs": queryset,
        "contacts": contact,
    }
    model = Post
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        blog_posts = self.queryset
        contacts = self.contact
        context["blog_posts"] = blog_posts
        context["contacts"] = contacts

        return context


def get_event(request, event_id):
    events_real = Events.objects.all()[:10]
    event = Events.objects.get(id=event_id)
    contact = MahnazContacts.objects.all()
    ctx = {
        "title": event.event_name,
        "content": event.event_description,
        "image": event.event_image,
        "event_id": event.id,
        "location": event.venue,
        "events": events_real,
        "contacts": contact,
    }
    return render(request, "event.html", ctx)


def get_image_details(request, image_id):
    our_image = OurImages.objects.all()[:20]
    image = OurImages.objects.get(id=image_id)
    contact = MahnazContacts.objects.all()
    ctx = {
        "image": image.image,
        "date": image.uploaded_at,
        "name": image.img_name,
        "description": image.description,
        "ourimages": our_image,
        "contacts": contact,
    }
    return render(request, "blog/image_details.html", ctx)


def my_page_not_found(request, exception):
    return render(request, "exceptions/404.html", status=404)


def my_page_maintenance(request):
    return render(request, "exceptions/500.html", status=500)


def my_page_forbidden(request, exception):
    return render(request, "exceptions/403.html", status=403)
