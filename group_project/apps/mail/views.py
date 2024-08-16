# apps/mail/views.py

from django.shortcuts import render, redirect
from .forms import MailForm
from .models import Mail
from django.shortcuts import render, get_object_or_404


def mail_list(request):
    # To show received mails for the user
    received_mails = Mail.objects.filter(recipient=request.user.email, is_sent=False)
    sent_mails = Mail.objects.filter(sender=request.user.email, is_sent=True)
    
    context = {
        'received_mails': received_mails,
        'sent_mails': sent_mails
    }
    return render(request, 'new_mail_list.html', context)

def send_mail(request):
    if request.method == 'POST':
        form = MailForm(request.POST, request.FILES)
        if form.is_valid():
            mail = form.save(commit=False)
            mail.is_sent = True  # Mark this mail as sent
            mail.save()
            attachments = request.FILES.getlist('attachments')
            for file in attachments:
                # Attachments processing logic here
                pass
            return redirect('mail:mail_list')
    else:
        form = MailForm()
    
    return render(request, 'compose_mail.html', {'form': form})

def mail_detail(request, mail_id):
    mail = get_object_or_404(Mail, id=mail_id)
    return render(request, 'mail_detail.html', {'mail': mail})