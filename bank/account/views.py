from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


from .forms import UserForm
from .forms import User
# Create your views here.

def home(request):
    return render(request, 'account/home.html')

def registerPage(request):
    form =  UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        try :
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('first_name')
                messages.success(request,'Account was created for '+user)
                return redirect('login')
        except Exception as e:
            return HttpResponse(e)
    info = {'form' : form}
    return render(request,'account/register.html', info)

def loginPage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(f"Email : {email}")
        print(f"Password : {password}")
        user = User.objects.filter(email = email).values()
        #user = authenticate(email = email, password = password)
        print(user)
        if user is not None:
            login(request,user)
            info = {'email' : email}
            return redirect('home',email = email)
        else:
            messages.info(request, 'Username or Password is incorrect')
    return render(request,'account/login.html')

def logoutPage(request):
    logout(request)
    return redirect('login')

