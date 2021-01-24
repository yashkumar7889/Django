from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")

        else:
            messages.warning(request, "Invali Login")
            return render(request,'login.html')
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        username=request.POST["username"]
        email=request.POST["email"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.success(request, 'Username already taken')
                return render(request,'register.html')
            elif User.objects.filter(email=email).exists():
                messages.success(request, 'Email Already taken')
                return render(request,'register.html')
            else:
                user=User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)                         
                user.save()
                return redirect('login')
        else:
            messages.success(request, 'Password Not Matching')
            return render(request,'register.html')
        return redirect('/')
    else:    
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')