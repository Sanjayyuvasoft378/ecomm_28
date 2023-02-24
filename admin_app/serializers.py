from rest_framework import serializers
from admin_app.models import *

class MaincategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCategory
        fields  = ['id','category_name','description','image']
        
class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields  = ['id','main_category_id','category_name','description','image']
        
class ChildcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildCategory
        fields  = ['id','main_category_id','sub_category_id','category_name','description','image']
        
        
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','main_category_id','sub_category_id','product_name','description','image','price','qty']