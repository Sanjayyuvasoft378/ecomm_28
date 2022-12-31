from django.urls import path
from Ecomm_app import views
from .views import *
from .forms import *
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('index/', views.index),
    path('profile/', views.profileupdate),
    path('about/', views.about),
    path('contact/', views.contact),
    path('login/', views.CustomerLoginView.as_view(), name='login'),
    # path('registrations/',views.registration),
    path('category/<slug:val>', views.CategoryView.as_view(), name='category'),
    path('categorytitle/<val>', views.CategoryTitle.as_view(), name='categorytitle'),
    path('productDetail/<int:pk>',
         views.ProductDetail.as_view(), name='ProductDetail'),
    # path('userregistration/',views.RegistrationAPI.as_view(),name='userregistration'),
    # path('userlogin/',views.LoginAPI.as_view(),name='userlogin'),
    path('logout/', views.logout_view, name='logout'),
    path('contactus/', views.ContactusAPI.as_view(), name='contactus'),
    path('profileupdate/', views.UpdateProfile.as_view(), name='profileupdate'),
    path('productlist/', views.ProductListAPI.as_view(), name='productlist'),
    path('addtocart/', views.AddToCartAPI.as_view(), name='addtocart'),
    path('profileview/<int:pk>', views.ProfileViewAPI.as_view(), name='profileview'),
    path('changepassword/', views.changepassword, name='changepassword'),
    path('ChangePasswordAPI/', views.ChangePasswordAPI.as_view(),
         name='ChangePasswordAPI'),
    path('OrderAPI/', views.OrderAPI.as_view(), name='OrderAPI'),
    path('orderlist/', views.orderlistapi.as_view(), name='orderlist'),
    path('CartList/', views.CartList.as_view(), name='CartList'),
    path('cartdata/', views.cartdata, name='cartdata'),
    path('searchdata/', views.filter, name='searchdata'),
    path('addwishlist/', views.AddToWishlistAPI.as_view(), name='addwishlist'),
    path('wishlist/', views.WishlistAPI.as_view(), name='wishlist'),



    path('registrations/', views.CustomerRegistrationView.as_view(),
         name='registration'),
    path('accounts/login/', auth_view.LoginView.as_view(template_name='app/login.html',
         authentication_form=LoginForm), name='login'),
    path('password-reset/',auth_view.PasswordResetView.as_view(template_name="app/password_reset.html",form_class=PasswordResetForm), name="password-reset"),

]
