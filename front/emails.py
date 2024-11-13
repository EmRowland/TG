from django.core.mail import EmailMessage
from django.template.loader import render_to_string


def SendAdminMail(username, sender, message):
    to = ["admin@mahnazfinearts.com"]

    mail_subject = f"{username} just sent you a message from the contact form"
    message = render_to_string(
        "email/contact_admin.html",
        {
            "subject": mail_subject,
            "email": sender,
            "message": message,
        },
    )
    to_email = to
    email = EmailMessage(mail_subject, message, to=[to_email])
    print("send .........")
    email.send()
