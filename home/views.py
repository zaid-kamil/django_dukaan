from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Your message has been sent!')
        else:
            messages.error(request, '⚠️ Please fill in the form correctly!.')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form':form})