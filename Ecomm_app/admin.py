from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','title','selling_price','discount_price',
                    'description','composition','prodapp','category',
                    'product_image']
    
@admin.register(UserRegistration)
class UserRegistration(admin.ModelAdmin):
    list_display = ['id','username','email','password1','password2']

@admin.register(ContactUs)
class ConatctAdmin(admin.ModelAdmin):
    list_display = ['id','username','email','subject','your_message']