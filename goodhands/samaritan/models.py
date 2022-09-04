from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    id = models.BigAutoField()
    name = models.CharField(max_length=60, unique=True)

class Institution(models.Model):
    fund = 'fund'
    non_gov_org = 'non_gov_org'
    local = 'local'
    TYPE_CHOICES =[
        (fund, 'Fundacja'),
        (non_gov_org, 'Organizacja pozarządowa'),
        (local, 'Zbiórka lokalna')
    ]

    id = models.BigAutoField()
    name = models.CharField(max_length=60, unique=True)
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=15, choices=TYPE_CHOICES, default=fund)
    categories = models.ManyToManyField(Category)

class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.PROTECT)
    address = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    zip_code = models.CharField(max_length=10)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.CharField(max_length=120)
    user = models.ForeignKey(User, blank=True, default=None)
