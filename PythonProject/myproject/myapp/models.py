from django.db import models
#
class Subscriber(models.Model):
    chat_id = models.BigIntegerField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat id: {self.chat_id}"
