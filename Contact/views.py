from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from .forms import ContactForm
from django.core.mail import send_mail,BadHeaderError
from django.conf import settings
from .models import Contact
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def emailView(request):
    if request.method =="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            content=form.cleaned_data['content']
            form.save()
            messages.success(request,"Başarıyla gönderildi")
            return redirect('post:index')
    else:
        form=ContactForm()
    return render(request,"Contact.html",{"form":form})
# Create your views here.
