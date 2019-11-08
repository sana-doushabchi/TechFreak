from django.contrib.auth.models import User
from django.shortcuts import render


def home(request):
    return render(request, "index.html")


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
            return render(request, "signup.html", {"error_pass": error_pass})
        if User.objects.filter(username=username).exists():
            error_user = True
            return render(request, "signup.html" , {"error_user": error_user})
        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email)
        user.set_password(password1)
        user.save()
        return render(request, "index.html")
    return render(request, "signup.html")