# apps/mail/models.py

from django.db import models
from django.conf import settings

class Attachment(models.Model):
    file = models.FileField(upload_to='attachments/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name

class Mail(models.Model):
    # Add a sender field to differentiate between sent and received mail
    sender = models.EmailField(default=settings.DEFAULT_FROM_EMAIL)
    recipient = models.EmailField()
    cc = models.EmailField(blank=True, null=True)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    attachments = models.ManyToManyField(Attachment, blank=True)
    sent_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    is_sent = models.BooleanField(default=False)  # New field to differentiate between sent and received mails

    def __str__(self):
        return self.subject