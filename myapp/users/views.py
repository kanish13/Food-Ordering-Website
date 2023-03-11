from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get("username")
            messages.success(request,f'Welcome {username} successfully register')
            return redirect('index')
    else:
        form=UserCreationForm()
    return render(request,'register.html',{'form':form})