from django.shortcuts import render, redirect
from accounts.models import Profile
from django.http import HttpResponseRedirect
from accounts.forms import ProfileForm
from . forms import *
# Create your views here.

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('images')
    
    else:
        form = ImageForm

    return render(request, 'portfolio/image.html', {'form':form})
    