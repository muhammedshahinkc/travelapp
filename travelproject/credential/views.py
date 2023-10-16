from django.contrib import messages, auth

from django.contrib.auth.models import User

from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=="POST":
        uname = request.POST['user name']
        password = request.POST['password']
        user=auth.authenticate(username=uname,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def registration(request):
    if request.method=="POST":
        uname=request.POST['user name']
        fname = request.POST['first name']
        lname = request.POST['last name']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password==password1:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"user name taken")
                return redirect('registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
            else:
                user=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=password)
                user.save()
                return redirect('login')

        else:
             messages.info(request,"password not matching")
             return redirect("registration")
        return redirect('/')
    return render(request, "register.html", )
