from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField

# Create your models here.
class Product(models.Model):
    category = models.CharField(max_length=150)
    title = models.CharField(max_length=100)
    price = models.CharField(max_length=13)
    image = models.ImageField(upload_to='items/', blank = True)
    discount = models.CharField(max_length=20)
    description = models.TextField()
    status = models.BooleanField()
    date_created = models.DateField(auto_now_add=True)
    unique_id = models.CharField(max_length=100)
    
    
    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title
