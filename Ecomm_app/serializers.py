from rest_framework import serializers
from Ecomm_app.models import *

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistration
        fields = '__all__'
        
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistration
        fields = ['email','password1']
        
class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'
        
class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistration
        fields = ['username','email']
        
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'