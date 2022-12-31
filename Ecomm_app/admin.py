from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','title','selling_price','discount_price',
                    'description','composition','prodapp','category',
                    'product_image']
    
# @admin.register(UserRegistration)
# class UserRegistration(admin.ModelAdmin):
#     list_display = ['id','username','email','password1','password2']

@admin.register(ContactUs)
class ConatctAdmin(admin.ModelAdmin):
    list_display = ['id','username','email','subject','your_message']

@admin.register(AddToCartModel)
class AddToCart(admin.ModelAdmin):
    list_display = ['title','description','qty','selling_price','discount_price']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','product_title','qty','price']



@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ['title','qty','discount_price','product_image']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id','user','locality','name','state','zipcode']