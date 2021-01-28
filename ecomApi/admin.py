from django.contrib import admin
from .models import Product
from .models import Slider
from .models import User
from .models import Category
from .models import Orders
from .models import Googleuser
# show with spac
class adminproducts(admin.ModelAdmin):
    list_display = ['id','name','Category']

class adminusers(admin.ModelAdmin):
    list_display = ['id','username','email']

class admincate(admin.ModelAdmin):
    list_display = ['id','name']

class admingusers(admin.ModelAdmin):
    list_display = ['id','email']

class adminorders(admin.ModelAdmin):
    list_display = ['user','id','date']
# Register your models here.
admin.site.register(Product,adminproducts)
admin.site.register(Slider)
admin.site.register(User,adminusers)
admin.site.register(Category,admincate)
admin.site.register(Orders,adminorders)
admin.site.register(Googleuser,admingusers)

