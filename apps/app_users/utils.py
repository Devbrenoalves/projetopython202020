from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

def send_welcome_email(user_email, user_name):

    subject = "Welcome to Bloome! 🥳 "
    # message = f"Hi {user_name},\n\nWelcome to Bloome! We're excited to have you on board. Feel free to explore and connect with others.\n\nBest regards,\nThe Bloome Team"
    message=''
    # from_email = settings.EMAIL_HOST_USER
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user_email]
    html_body = render_to_string(
        "emails/welcome.html",
        {
            "user": user_name,
            "login_url": f"{settings.LIVE_SITE_URL_RN}{settings.LOGIN_URL}",
        }
    )

    send_mail(subject, 
              message, 
              from_email, 
              recipient_list,
              html_message=html_body,   
              )
