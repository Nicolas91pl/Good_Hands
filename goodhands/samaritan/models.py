from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=60, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Institution(models.Model):
    fund = 'fund'
    non_gov_org = 'non_gov_org'
    local = 'local'
    TYPE_CHOICES =[
        (fund, 'Fundacja'),
        (non_gov_org, 'Organizacja pozarządowa'),
        (local, 'Zbiórka lokalna')
    ]

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=60, unique=True)
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=15, choices=TYPE_CHOICES, default=fund)
    categories = models.ManyToManyField(Category)
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Donation(models.Model):
    id = models.BigAutoField(primary_key=True)
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.PROTECT)
    address = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    zip_code = models.CharField(max_length=10)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.CharField(max_length=120)
    # phone = models.CharField(max_length=12)
    user = models.ForeignKey(User, blank=True, default=None, on_delete=models.PROTECT)
