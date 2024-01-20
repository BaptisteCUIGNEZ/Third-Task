
from django.db import models

class Message(models.Model):
    sender = models.CharField(max_length=50, default="DefaultSender")
    recipient = models.CharField(max_length=50, default='DefaultValue')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.sender} to {self.recipient}: {self.content}"



