from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User

class LandingPage(View):
    def get(self, request):
        return render(request, "index.html")

class AddDonation(View):
    def get(self, request):
        return render(request, "form.html")

class Login(View):
    def get(self, request):
        return render(request, "login.html")

class Register(View):
    def get(self, request):
        return render(request, "register.html")

    def post(self, request):
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        if password == password2:
            User.objects.create(username=email, first_name=name, last_name=surname, email=email, password=password)
            return redirect(f'/login')
