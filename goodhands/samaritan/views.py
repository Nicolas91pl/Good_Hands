from django.shortcuts import render, redirect
from django.views import View
from samaritan.models import Donation, Institution, Category
from django.contrib.auth.models import User

class LandingPage(View):
    def get(self, request):
        donations = list(Donation.objects.all())
        organizations = list(Institution.objects.all())
        quantity_sum = 0
        for don in donations:
            quantity_sum = quantity_sum + int(don.quantity)

        organization_sum = len(organizations)
        
        fundations = list(Institution.objects.filter(type='fund'))
        non_gov_orgs = list(Institution.objects.filter(type='non_gov_org'))
        local_gathering = list(Institution.objects.filter(type='local'))

        ctx = {
            "quantity_sum": quantity_sum,
            "organization_sum": organization_sum,
            'fundations': fundations,
            'non_gov_orgs': non_gov_orgs,
            'local_gathering': local_gathering
            }
     
        return render(request, "index.html", ctx)

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
