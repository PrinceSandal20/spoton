from email.policy import default
from turtle import width
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from numpy import outer

class RentIn(models.Model):
    name = models.CharField(max_length=200,db_index=True)
    image = models.ImageField(default='product/images/default.jpg',upload_to='product/images/')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    date_rentIn = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name  

    def save(self,**kwargs):
        super().save()
        
        img = Image.open(self.image.path)
        
             

    def get_absolute_url(self):
        return reverse('rentIn-detail',kwargs={'pk':self.pk})
    		

