from django.contrib.auth.models import User
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, logout


def home(request):
    is_authenticated = False
    if request.user.is_authenticated:
        is_authenticated = True
    return render(request, "index.html" ,{'is_authenticated':is_authenticated})


def signup(request):
    if request.method == 'POST':
        error_pass = False
        error_user = False
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1 != password2 :
            error_pass = True
        if User.objects.filter(username=username).exists():
            error_user = True
        if error_user or error_pass:
            return render(request, "signup.html", {"error_user": error_user, "error_pass": error_pass})
        user = User(first_name=first_name, last_name=last_name, username=username, email=email)
        user.set_password(password1)
        user.save()
        return render(request, "index.html")
    return render(request, "signup.html")


def log_in(request):
    if request.method == 'POST':
        error = False
        username = request.POST.get("username")
        password = request.POST.get("password")
        if User.objects.filter(username=username).exists():
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
            else:
                return render(request, 'login.html', {"error": True})
            return redirect('/')
        else:
            return render(request, 'login.html', {"error": True})
    return render(request,'login.html')


def contactus(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        email = request.POST.get("email")
        text = request.POST.get("text")
        if not len(str(text)) < 10 or len(str(text)) > 250 :
            return render(request, "contactdone.html")
    return render(request, "contactus.html")


def log_out(request):
    logout(request)
    return render(request, "index.html")



