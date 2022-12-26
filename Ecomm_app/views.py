from django.shortcuts import render, redirect
from .serializers import *
from django.views import View
from rest_framework import status
from .models import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate
from .forms import *

def index(request):
    return render(request, "app/home.html")

def about(request):
    return render(request, "app/about.html")

def contact(request):
    return render(request, "app/contact.html")

def profileupdate(request):
    return render(request, 'app/profile.html')

# def registration(request):
#     return render(request,'app/registration.html')


class CustomerRegistrationView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "app/registration.html", locals())


class CustomerLoginView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "app/login.html", locals())


class RegistrationAPI(APIView):
    def post(self, request, *args, **kwargs):
        try:
            form = UserRegistrationSerializer(data=request.data)
            if form.is_valid():
                form.save()
                return redirect('/ecomm_app/login/')
            else:
                return redirect('/ecomm_app/registrations/')
        except Exception as e:
            return redirect('/ecomm_app/registrations/')


class LoginAPI(APIView):
    def post(self,request, *args, **kwargs):
        email = request.data.get('email',None)
        password1 = request.data.get('password1',None)
        print("email",email,"password",password1)
        try:
            get_data = UserRegistration.objects.get(email=email, password1=password1)
            if get_data:
                return redirect('/ecomm_app/index/')
            else:
                return redirect('/ecomm_app/registrations/')
        except Exception as e:
            return redirect('/ecomm_app/registrations/')

class ContactusAPI(APIView):
    def post(self, request):
        try:
            Serializer = ContactUsSerializer(data=request.data)
            if Serializer.is_valid():
                Serializer.save()
                return redirect('/ecomm_app/index/')
            else:
                return redirect('/ecomm_app/contactus/')
        except Exception as e:
            return redirect('/ecomm_app/contactus/')

class CategoryView(View):
    def get(self, request, val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request, "app/category.html", locals())


class CategoryTitle(View):
    def get(self, request, val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(
            category=product[0].category).values('title')
        return render(request, 'app/category.html', locals())


class ProductDetail(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html', locals())

class UpdateProfile(APIView):
    def post(self, request,pk):
        try:
            get_data = UserRegistration.objects.get(pk=pk)
            serializers = UserRegistrationSerializer(instance=get_data, data=request.data)
            if serializers.is_valid():
                serializers.save()
                return redirect('/ecomm_app/index/')
            else:
                return redirect('/ecomm_app/index/')
        except Exception as e:
            return redirect('/ecomm_app/index/')
        
class ProductListAPI(APIView):
    def get(self, request):
        try:
            get_data = Product.objects.all()
            Serializer = ProductSerializer(get_data, many=True)
            return JsonResponse(Serializer.data, safe=False,status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({"mesg":"Internal server error {}".format(e)},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)




