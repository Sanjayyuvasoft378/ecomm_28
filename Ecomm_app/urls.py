from django.urls import path
from Ecomm_app import views
from .views import *

urlpatterns = [
    path('index/',views.index), 
    path('profile/',views.profileupdate),
    path('about/',views.about), 
    path('contact/',views.contact), 
    path('registrations/',views.CustomerRegistrationView.as_view(),name='registration'),
    path('login/',views.CustomerLoginView.as_view(),name='login'),
    # path('registrations/',views.registration),
    path('category/<slug:val>',views.CategoryView.as_view(),name='category'),
    path('categorytitle/<val>',views.CategoryTitle.as_view(),name='categorytitle'),
    path('productDetail/<int:pk>',views.ProductDetail.as_view(),name='ProductDetail'),
    path('userregistration/',views.RegistrationAPI.as_view(),name='userregistration'),
    path('userlogin/',views.LoginAPI.as_view(),name='userlogin'),
    path('contactus/',views.ContactusAPI.as_view(),name='contactus'),
    path('profileupdate/',views.UpdateProfile.as_view(),name='profileupdate'),
    path('productlist/',views.ProductListAPI.as_view(),name='productlist'),
]
 



