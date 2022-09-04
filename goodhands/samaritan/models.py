from django.db import models

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
