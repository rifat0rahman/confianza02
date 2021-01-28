from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import AbstractUser
import datetime
import random
# Create your models here.
# category class
class Category(models.Model):
    name = models.CharField(max_length=50)
    descriptions = models.TextField(max_length=400)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
# color choices variable
colors = (('black','black'),('white','white'),('red','red'),('blue','blue'),
        ('pink','pink'),('grey','grey'))
sizes = (('S','S'),('M','M'),('L','L'),('xl','xl'))

class Product(models.Model):
    name =  models.CharField(max_length=70)
    price = models.IntegerField(default=0)
    details= models.TextField(max_length=300)
    pro_image1 = models.ImageField(upload_to='images')
    pro_image2 = models.ImageField(upload_to='images')
    pro_image3 = models.ImageField(upload_to='images')
    colors = MultiSelectField(choices=colors)
    sizes = MultiSelectField(choices=sizes)
    Category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    class Meta:
        ordering = ['-timestamp']

class Slider(models.Model):
    sliderimage1 = models.ImageField(upload_to='images')
    sliderimage2 = models.ImageField(upload_to='images')
    sliderimage3 = models.ImageField(upload_to='images')

class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=254,unique=True)
    phone = models.IntegerField(null = True)
    name = models.CharField(max_length=50)
    REQUIRED_FIELDS = ['name','username','phone','password']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email

def random_string():
    return str(random.randint(10000, 99999))

class Orders(models.Model):
    user = models.CharField(max_length=50)
    cart =models.TextField(null=True,blank=True)
    Placement = models.TextField(null=True)
    pricing = models.TextField(null=True,blank=True)
    id = models.CharField(default=random_string,primary_key=True,max_length= 6)
    date = models.DateField(default=datetime.date.today)
    status = models.BooleanField(default=False)
    quantities = models.IntegerField(default=1)
    address = models.CharField(max_length=50,default='null')

class Googleuser(models.Model):
    userid = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=11)
    email = models.EmailField(max_length=254)
    username = models.CharField(max_length=256)