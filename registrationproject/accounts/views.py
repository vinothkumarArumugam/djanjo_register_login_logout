from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout




def register(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=UserCreationForm()
    return render(request,'registration/register.html',{'form':form})  

def login_user(request):
    if request.method == 'POST' :
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('success')
    else :
        form=AuthenticationForm()
    return render(request,'registration/login.html',{'form':form})

def logout_user(request):
    logout(request)
    return redirect('login')
 
def success(request) :
    return render(request,'accounts/registration/success.html')
             

# Create your views here.
