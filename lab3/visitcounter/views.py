from django.shortcuts import render
from .models import Visit

def home(request):
    visit, created = Visit.objects.get_or_create(id=1)
    visit.count += 1
    visit.save()
    return render(request, 'visitcounter/home.html', {'visit_count': visit.count})