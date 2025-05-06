from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.utils import timezone
from pytz import timezone as pytz_timezone
from .bot import send_login_notification

@receiver(user_logged_in)
def on_user_login(sender, request, user, **kwargs):
    if user.is_staff or user.is_superuser:

        utc_now = timezone.now()

        target_timezone = pytz_timezone('Etc/GMT-5')
        login_time = utc_now.astimezone(target_timezone)

        login_time_str = login_time.strftime("%Y-%m-%d %H:%M:%S")

        send_login_notification(user.username, login_time_str)