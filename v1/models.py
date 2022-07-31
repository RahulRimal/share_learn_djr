from statistics import mode
from django.db import models

# Create your models here.



class Book(models.Model):
    book_name = models.CharField(max_length=256, null=False)
    author = models.CharField(max_length=256, null=True, blank= True)
    description = models.CharField(max_length=256, null=True, blank= True)
    bought_date = models.DateField(auto_now_add=True)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    # cover_picture = 
    # pictures = 
    created_on = models.DateTimeField(auto_now_add=True)