from django.shortcuts import render
from .models import Section


# Create your views here.
def index(request):
    sections = Section.objects.all().order_by('depth_string')
    context = {'sections': sections}
    return render(request, 'rules/index.html', context)