from django import forms
from .models import Mail

class MailForm(forms.ModelForm):
    attachments = forms.FileField(required=False)

    class Meta:
        model = Mail
        fields = ['recipient', 'cc', 'subject', 'body', 'attachments']
        widgets = {
            'body': forms.Textarea(attrs={'rows': 6}),
        }