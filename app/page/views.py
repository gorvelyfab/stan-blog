from django.conf import settings
from django.urls import reverse
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages

from app.portfolio.models import Work
from .forms import ContactForm


def index(request):
    works = Work.objects.all()
    return render(request, 'page/index.html', {'works': works})


def about(request):
    return render(request, 'page/about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            # name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            content = form.cleaned_data['content']

            recipients = [settings.STAN_EMAIL]

            send_mail(subject, content, email, recipients)

            messages.success(request, 'Success, your message has been sent')
            return redirect(reverse('page:index'))

    form = ContactForm
    return render(request, 'page/contact.html', {'form': form})
