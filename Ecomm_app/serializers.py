from rest_framework import serializers
from Ecomm_app.models import *

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistration
        fields = '__all__'
        
# class LoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserRegistration
#         fields = ['email','password1']
        
class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'
        
# class ProfileUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserRegistration
#         fields = ['username','email']
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        

class AddToCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddToCartModel
        fields = ['product_id','qty']    
        
class ChangePasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistration
        fields = ['password1','password2']
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['product_title','qty','price']

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = "__all__"

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['id','first_name','last_name','email','mobile_no','gender']


