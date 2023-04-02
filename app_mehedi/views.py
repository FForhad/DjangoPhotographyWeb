from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    return render(request, 'home.html')
def login_user(request):
    if request.method=="POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            return redirect('home')
             
        else:
            messages.error(request, "Bad Credentials!")
            return redirect('login')

    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist")
            return redirect('home')
        if User.objects.filter(email=email):
            messages.error(request, "email already registered")
            return redirect('home')
        if pass1 != pass2:
            messages.error(request, "Password didnot match")

        myuser = User.objects.create_user(username,email,pass1)
        myuser.save()

        messages.success(request, "Your Account has been sucessfully created.")
        return redirect('login')
    return render(request, 'register.html')

def signout(request):
    logout(request)
    messages.error(request, "Logged Out Successfully!")
    return redirect('home')

def nature(request):
    return render(request, 'nature.html')
def animal(request):
    return render(request, 'animal.html')
def portrait(request):
    return render(request, 'portrait.html')
def lifestyle(request):
    return render(request, 'lifestyle.html')
    