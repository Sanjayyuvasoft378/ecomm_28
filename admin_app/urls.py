from django.urls import path
from admin_app import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    
    path('home/',views.home,name='home'),
    path('allproductlist/',views.allproductlist,name='allproductlist'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('allorder/',views.allorder,name='allorder'),
    path('pending-order/',views.pendingorder,name='pending-order'),
    path('processing-order/',views.processingorder,name='processing-order'),
    path('completed-order/',views.completedorder,name='completed-order'),
    path('decliend-order/',views.deciendorder,name='decliend-order'),
    path('deactivate-product/',views.deactivateproduct,name='deactivate-product'),
    path('add-product/',views.addproduct,name='add-product'),
    
    path('product-reviews/',views.productreviews,name='product-reviews'),
    path('product-comments/',views.productcomments,name='product-comments'),
    path('product-reports/',views.productreports,name='product-reports'),
    path('coupons/',views.coupons,name='coupons'),
    
    
    path('api/v1/main-category/',views.MainCategoryAPI.as_view(),name='main-category'),
    path('api/v1/main-category/<int:pk>',views.MainCategoryAPI.as_view(),name='main-category'),
    
    path('api/v1/sub-category/',views.SubCategoryAPI.as_view(),name='sub-category'),
    path('api/v1/sub-category/<int:pk>',views.SubCategoryAPI.as_view(),name='sub-category'),
    
    path('api/v1/child-category/',views.ChildCategoryAPI.as_view(),name='child-category'),
    path('api/v1/child-category/<int:pk>',views.ChildCategoryAPI.as_view(),name='child-category'),
    
    path('api/v1/product/',views.ProductAPI.as_view(),name='product'),
    path('api/v1/product/<int:pk>',views.ProductAPI.as_view(),name='product'),
    
    path('api/v1/product-list/',views.ProductlistAPI.as_view(),name='product-list'),
    
]