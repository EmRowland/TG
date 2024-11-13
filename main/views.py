from django.shortcuts import render, redirect
from django.http import HttpResponse
from .subform import SubForm
from .models import Subscribers, SubscribeToEvent, Events
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib import messages
from .cronjob import cronjob

# Create your views here.


def subscribe(request):
    form = SubForm(request.POST)
    subject = "Welome to Manhza"
    try:
        if request.method == "POST":
            form = Subscribers()
            user_email = request.POST["user_email"]
            form.user_email = request.POST["user_email"]
            if Subscribers.objects.filter(user_email=user_email):
                messages.error(request, "You are already subscribed to this service")
                cronjob()
                return redirect("home")
            if not form.user_email:
                messages.error(request, "Email field can not be empty")

                return redirect("home")
            else:
                username = user_email.split("@")[0]
                message = "We are glad you subscribed to our news later \n Thank you"
                form.save()
                mail_subject = subject
                message = render_to_string(
                    "email/sub.html",
                    {
                        "subject": mail_subject,
                        "username": username,
                        "email": user_email,
                        "message": message,
                    },
                )
                to_email = user_email
                email = EmailMessage(mail_subject, message, to=[to_email])

                email.send()
                messages.success(request, "You are Now subscribed to our Newsletter")
                return redirect("home")
    except Exception:
        messages.error(request, "Something Went Wrong")

        return redirect("home")

    return HttpResponse("Something Went Wrong")


def subscribe_to_events(request):
    if request.method == "POST":
        form = SubscribeToEvent()
        event_id = request.POST["event_id"]
        user_mail = request.POST["event_email"]
        status = "True"
        try:
            event = Events.objects.get(id=event_id)
            sub = SubscribeToEvent.objects.create(
                status=status,
                # event=event,
                subscribed_user_email=user_mail,
            )
            sub.event.add(event)
        except Exception:
            return redirect("home")
        return redirect("home")


def subscribe_to_eventss(request):
    if request.method == "POST":
        form = SubscribeToEvent()
        user_mail = request.POST["event_email"]
        event_id = request.POST["event_id"]

        email_exist = SubscribeToEvent.objects.filter(subscribed_user_email=user_mail)
        eventid = Events.objects.get(id=event_id)
        try:
            if not user_mail:
                messages.error(request, "Email Field Can not Be Empty")
                return redirect("home")
            elif email_exist:
                messages.error(request, "You are already subscribed to this service")
                return redirect("home")
            elif not eventid:
                messages.error(request, "Event Does Not Exist")
                return redirect("home")

            else:
                subject = "Subscribtion to an Event"
                username = user_mail.split("@")[0]
                message = "We are glad you subscribed to our news later \n Thank you"
                status = "True"
                event = form.event.set(id=event_id)
                form.subscribed_user_email = user_mail
                form.status = status
                form.event = event_id

                form.add()
                mail_subject = subject
                message = render_to_string(
                    "email/sub.html",
                    {
                        "subject": mail_subject,
                        "username": username,
                        "email": user_mail,
                        "message": message,
                    },
                )
                to_email = form.user_email
                email = EmailMessage(mail_subject, message, to=[to_email])
               
                email.send()
                messages.success(request, "You are Now subscribed to our Newsletter")
                return redirect("home")
        except Exception:
            return redirect("home")
