from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm        #### these are built in methods for user registrstion creation
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login                        ### we have to import these from django.contrib.auth(authentication)
from django.contrib.auth import logout




def register(request):
    if request.method == 'POST':                   ### if method method == post it will satisfy this condition 
        form=UserCreationForm(request.POST)        ## usercreationform is built in it will automatically create fields in database
        if form.is_valid():
            form.save()
            return redirect('login')         ##it will redirect to login path(urls)  you have to mention its name in urls path
    else:
        form=UserCreationForm()
    return render(request,'registration/register.html',{'form':form}) ## use registration in templates directory  

def login_user(request):
    if request.method == 'POST' :
        form=AuthenticationForm(request,request.POST)   ### here it will authenticate entered information (checking)
        if form.is_valid():
            user=form.get_user()
            login(request,user)     ## it make user to log in 
            return redirect('success')  ## this redirect to success in urls path
    else :
        form=AuthenticationForm()
    return render(request,'registration/login.html',{'form':form})

def logout_user(request):
    logout(request)
    return redirect('login')
 
def success(request) :
    return render(request,'accounts/registration/success.html')
             

# Create your views here.
