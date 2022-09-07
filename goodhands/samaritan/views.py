from django.shortcuts import render
from django.views import View
from samaritan.models import Donation, Institution, Category

class LandingPage(View):
    def get(self, request):
        fundations = list(Institution.objects.filter(type='fund'))
        non_gov_orgs = list(Institution.objects.filter(type='non_gov_org'))
        local_gathering = list(Institution.objects.filter(type='local'))
        ctx = {
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
