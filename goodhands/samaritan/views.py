from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from samaritan.models import Donation, Institution, Category
from django.contrib.auth.models import User

class LandingPage(View):
    def get(self, request):
        # def get_categories(institution_obj):
        #     categories = list(institution_obj.categories.all())
        #     cat_name_list = []
        #     for category in categories:
        #         cat_name_list.append(category.name)
        #     return ", ".join(cat_name_list)

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
            'local_gathering': local_gathering,
            }
     
        return render(request, "index.html", ctx)

class AddDonation(View):
    def get(self, request):
        if request.user.is_authenticated:
            categories = list(Category.objects.all())
            ctx = {
                "categories": categories,
            }
            return render(request, "form.html", ctx)
        else:
            return redirect('/login')

    def post(self, request):
        categories = request.POST.get("categories")
        bags = request.POST.get("bags")
        organization = request.POST.get("organization")
        address = request.POST.get('address')
        city = request.POST.get('city')
        postcode = request.POST.get('postcode')
        phone = request.POST.get('phone')
        data = request.POST.get('data')
        time = request.POST.get('time')
        more_info = request.POST.get('more_info')
        return Donation.objects.create(quantity=bags, categories=categories,
                                       institution=organization, address=address,
                                       city=city, zip_code=postcode, pick_up_date=data,
                                       pick_up_time=time, pick_up_comment=more_info
                                        )


class Login(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/start')
        else:
            return redirect('/register')

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('/start')

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

class Profil(View):
    def get(self, request):
        if request.user.is_authenticated:
            user = request.user.id
            donations = list(Donation.objects.filter(user=user))
            ctx = {
                'donations': donations,
                }
            return render(request, 'profil.html', ctx)
        else:
            return redirect(f'/login')
