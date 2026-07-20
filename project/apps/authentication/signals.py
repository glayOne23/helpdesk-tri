from django.dispatch import receiver
from allauth.account.signals import user_logged_in

from apps.services.session import setsession


@receiver(user_logged_in)
def set_session_on_social_login(request, user, **kwargs):
    setsession(request, user)
