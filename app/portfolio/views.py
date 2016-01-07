from django.shortcuts import render, get_object_or_404

from .models import Work


def index(request):
    works = Work.objects.all()
    return render(request, 'portfolio/index.html', {'works': works})


def show(request, slug):
    work = get_object_or_404(Work, slug=slug)
    return render(request, 'portfolio/show.html', {'work': work})
