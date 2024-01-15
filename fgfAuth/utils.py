# utils.py

from django.core.mail import send_mail
from django.template.loader import get_template
from django.conf import settings
from huey.contrib.djhuey import task

@task()
def send_email_verification(user, token):
    data = {
        "user_id": str(user.id),
        "token": str(token),
        "frontend_url": "https://fgfoundation.onrender.com",  # TODO: This should come from the settings
    }
    message = get_template("email_verification.txt").render(
        data
    )  # TODO: Replace with a professional email template
    send_mail(
        subject="Email Verification",
        message=message,
        from_email=None,
        recipient_list=[user.email],
    )
