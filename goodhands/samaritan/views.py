from django.shortcuts import render
from django.views import View
from samaritan.models import Donation, Institution

class LandingPage(View):
    def get(self, request):
        donations = list(Donation.objects.all())
        organizations = list(Institution.objects.all())
        quantity_sum = 0
        for don in donations:
            quantity_sum = quantity_sum + int(don.quantity)

        organization_sum = len(organizations)

        ctx = {
            "quantity_sum": quantity_sum,
            "organization_sum": organization_sum
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
