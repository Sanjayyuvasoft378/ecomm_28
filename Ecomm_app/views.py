from django.shortcuts import render, redirect
from .serializers import *
from django.views import View
from rest_framework import status
from .models import *
from rest_framework.views import APIView
from django.http import JsonResponse
from .forms import *
from django.contrib.auth import logout
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib import messages


    
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

def index(request):
    return render(request, "app/home.html")

def about(request):
    return render(request, "app/about.html")

def contact(request):
    return render(request, "app/contact.html")

def profileupdate(request):
    return render(request, 'app/profile.html')

def cartdata(request):
    return render(request, 'app/cartlist.html')
# def registration(request):
#     return render(request,'app/registration.html')

def changepassword(request):
    return render(request,'app/changepasword.html')


class CustomerRegistrationView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, "app/registration.html", locals())
    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Congrats ! User Registration successfully")
        else:
            messages.warning(request,"Invalid Form Data !! please enter correct data....")
        return render(request,'app/registration.html',locals())

class CustomerLoginView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "app/login.html", locals())
    


# class RegistrationAPI(APIView):
#     def post(self, request, *args, **kwargs):
#         try:
#             form = UserRegistrationSerializer(data=request.data)
#             if form.is_valid():
#                 form.save()
#                 return redirect('/ecomm_app/login/')
#             else:
#                 return redirect('/ecomm_app/registrations/')
#         except Exception as e:
#             return redirect('/ecomm_app/registrations/')


# class LoginAPI(APIView):
#     def post(self,request, *args, **kwargs):
#         email = request.data.get('email',None)
#         password1 = request.data.get('password1',None)
#         try:
#             login_data = UserRegistration.objects.get(email=email, password1=password1)
#             if login_data is not None:
#                 return redirect('/ecomm_app/index/')
#             else:
#                 return redirect('/ecomm_app/registrations/')
#         except Exception as e:
#             return redirect('/ecomm_app/registrations/')


def logout_view(request):
    logout(request)
    return redirect('/ecomm_app/login/')
    
  
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
        
    def get(self, request):
        try:
            get_data = ContactUs.objects.all()
            Serializer = ContactUsSerializer(get_data, many = True)
            return JsonResponse(Serializer.data,safe=False, status= status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({"msg":"Internal server error {}".format(e)},safe=False,
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request,pk):
        try:
            pk = ContactUs.objects.get(pk)
            serializer = ContactUsSerializer(pk = pk)
            serializer.delete()
            return JsonResponse({"msg":"data deleted successfully"},
                                safe=False,status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({"msg":"Internal server error {}".format(e)},safe=False,
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

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

class AddToCartAPI(APIView):
    def post(self, request):
        try:
            Serializer = AddToCartSerializer(data=request.data)
            if Serializer.is_valid():
                Serializer.save()
                # return redirect('/ecomm_app/cartlist/')
                return JsonResponse({"msg":"data added into cart"})
            else:
                # return redirect('/ecomm_app/productlist/')
                return JsonResponse({"msg":"data not added into cart"})
        except Exception as e:
            # return redirect('/ecomm_app/productlist/')
            return JsonResponse({"msg":"data not  500 added into cart{}".format(e)})

class ProfileViewAPI(APIView):
    def get(self, request,pk):
        try:
            profile_data = UserRegistration.objects.get(pk=pk)
            return render(request, 'app/profileview.html',locals())
        except Exception as e:
            return JsonResponse({"msg":"Internal server error {}".format(e)},
                                safe=False,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ChangePasswordAPI(APIView):
    def post(self, request):
        Serializer = ChangePasswordSerializer(data=request.data, context={"user":request.user})
        if Serializer.is_valid(raise_exception=True):
            Serializer.save()
            return redirect('/ecomm_app/userlogin/')
        else:
            return render(request,'app/changepasword.html')

class OrderAPI(APIView):
    def post(self, request, *args, **kwargs):
        try:
            Serializer = OrderSerializer(data=request.data)
            if Serializer.is_valid(raise_exception=True):
                Serializer.save()
                return JsonResponse({"msg":"Order created successfully"},safe=False)
            else:
                return JsonResponse({"msg":"Invalid data"},safe=False)
        except Exception as e:
            return JsonResponse({"msg":"Internal server error {}".format(e)},safe=False)
class orderlistapi(APIView):
    def get(self, request):
        try:
            get_data = Order.objects.all()
            serializer = OrderSerializer(get_data, many = True)
            return JsonResponse(serializer.data, safe=False)
        except Exception as e:
            return JsonResponse({"msg":"Internal server error {}".format(e)},safe=False)
      
class CartList(APIView):
    def get(self, request):
        cart_data = AddToCartModel.objects.all()
        # Serializer = AddToCartSerializer(cart_data, many=True)
        return render(request,'app/cartlist.html',locals())
        return JsonResponse(Serializer.data,safe=False)
             

def filter(request):
    if request.method=="POST":
        title = request.POST.get('title')
        emps = Product.objects.all()
        if title:
            products = emps.filter(title__icontains = title)
            context = {
                "emps":products
            }
            return render(request, "home.html",context)
        else:
            return JsonResponse({"msg":"Invalid input"})
    else:
        return JsonResponse({"msg":"invalid method"})
    
class AddToWishlistAPI(APIView):
    def post(self, request):
        try:
            Serializer = AddToCartSerializer(data=request.data)
            if Serializer:
                if Serializer.is_valid():
                    Serializer.save()
                    return JsonResponse({"msg":"Product added into wishlist"},safe=False)
                else:
                    return JsonResponse({"msg":"Invalid data"})
            else:
                return JsonResponse({"msg":"Serializer data invalid"})
        except Exception as e:
            return JsonResponse({"msg":"Internal server error {}".format(e)},safe=False)

class WishlistAPI(APIView):
    def get(self, request):
        try:
            get_data = Wishlist.objects.all()
            Serializer = WishlistSerializer(get_data, many=True)
            # return JsonResponse(Serializer.data, safe=False,status=status.HTTP_200_OK)
            return render(request,'app/wishlist.html', locals())
        except Exception as e:
            return JsonResponse({"msg":"Internal server error {}".format(e)}
                                ,safe=False,status=status.HTTP_500_INTERNAL_SERVER_ERROR)