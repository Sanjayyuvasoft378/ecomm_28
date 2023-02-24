from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from django.http import JsonResponse

def allproductlist(request):
    return render(request, 'Product/all_product.html')

def dashboard(request):
    return render(request,'dashboard.html')

def allorder(request):
    return render(request,'Order/allorder.html')

def pendingorder(request):
    return render(request,'Order/order_pending.html')

def processingorder(request):
    return render(request,'Order/processing_order.html')

def completedorder(request):
    return render(request,'Order/completed_order.html')

def deciendorder(request):
    return render(request,'Order/deciend_order.html')

def home(request):
    return render(request,'Product/add_product.html')

def deactivateproduct(request):
    return render(request,'Product/deactivate_product_list.html')

def addproduct(request):
    return render(request,'Product/add_product.html')

############

def productreviews(request):
    return render(request,'Product/product_reviews.html')



def productcomments(request):
    return render(request,'Product/product_comments.html')



def productreports(request):
    return render(request,'Product/product_reports.html')


def coupons(request):
    return render(request,'coupons.html')




# Create your views here.
class MainCategoryAPI(APIView):
    def post(self, request):
        try:
            Serializer = MaincategorySerializer(data=request.data)        
            if MainCategory.objects.filter(**request.data).exists():
                raise serializers.ValidationError("category already exist")
            if Serializer.is_valid():
                Serializer.save()
                # return render(request, 'Categories/Main-Category/main_category_list.html')
                return JsonResponse({"msg":"data added successfully"},safe=False,status=200)
            else:
                return JsonResponse({"msg":"invalid data "},safe=False,status=400)
        except Exception as e:
            return JsonResponse({"msg":"Internal server error {}".format(e)},safe=False, status=500)

    def get(self, request):
        item = MainCategory.objects.all()
        Serializer = MaincategorySerializer(item, many=True)
        data=Serializer.data
        return render(request, 'Categories/Main-Category/main_category_list.html',{"data":data})
        # return JsonResponse(Serializer.data,safe=False)
    
    def delete(self, request, pk):
        item = MainCategory.objects.filter(id=pk)
        item.delete()
        return JsonResponse({"msg":"delete"},safe=False)

    def put(self, request,pk):
        item = MainCategory.objects.get(pk=pk)
        Serializer = MaincategorySerializer(instance=item, data=request.data)
        if MainCategory.objects.filter(**request.data).exists():
            raise serializers.ValidationError("category of this name already exists")

        if Serializer.is_valid():
            Serializer.save()
            return JsonResponse({"msg":"category updated"},safe=False)
        else:
            return JsonResponse({"msg":"invalid form data"}, safe=False)


        
    
    
        
class SubCategoryAPI(APIView):
    def post(self, request):
        Serializer = SubcategorySerializer(data=request.data)
        if SubCategory.objects.filter(**request.data).exists():
            raise serializers.ValidationError("category already exist")
        if Serializer.is_valid():
            Serializer.save()
            return JsonResponse({"msg":"data added successfully"},safe=False)
        else:
            return JsonResponse({"msg":"invalid data "},safe=False)
    def get(self, request):
        item = SubCategory.objects.all()
        Serializer = SubcategorySerializer(item, many=True)
        data = Serializer.data
        return render(request,'Categories/Sub-Category/sub_category_list.html',{"data":data})
        # return JsonResponse(Serializer.data,safe=False)
    
    def delete(self, request, pk):
        item = SubCategory.objects.filter(id=pk)
        item.delete()
        return JsonResponse({"msg":"delete"},safe=False)

    def put(self, request,pk):
        item = SubCategory.objects.get(pk=pk)
        Serializer = SubcategorySerializer(instance=item, data=request.data)
        if SubCategory.objects.filter(**request.data).exists():
            raise serializers.ValidationError("category of this name already exists")

        if Serializer.is_valid():
            Serializer.save()
            return JsonResponse({"msg":"category updated"},safe=False)
        else:
            return JsonResponse({"msg":"invalid form data"}, safe=False)

        
class ChildCategoryAPI(APIView):
    def post(self, request):
        Serializer = ChildcategorySerializer(data=request.data)
        if ChildCategory.objects.filter(**request.data).exists():
            raise serializers.ValidationError("category already exist")
        if Serializer.is_valid():
            Serializer.save()
            return JsonResponse({"msg":"data added successfully"},safe=False)
        else:
            return JsonResponse({"msg":"invalid data "},safe=False)
    def get(self, request):
        item = ChildCategory.objects.all()
        Serializer = ChildcategorySerializer(item, many=True)
        data = Serializer.data
        return render(request,'Categories/Child-Category/child_category_list.html',{"data":data})
        # return JsonResponse(Serializer.data,safe=False)
    
    def delete(self, request, pk):
        item = ChildCategory.objects.filter(id=pk)
        item.delete()
        return JsonResponse({"msg":"delete"},safe=False)

    def put(self, request,pk):
        item = ChildCategory.objects.get(pk=pk)
        Serializer = ChildcategorySerializer(instance=item, data=request.data)
        if ChildCategory.objects.filter(**request.data).exists():
            raise serializers.ValidationError("category of this name already exists")

        if Serializer.is_valid():
            Serializer.save()
            return JsonResponse({"msg":"category updated"},safe=False)
        else:
            return JsonResponse({"msg":"invalid form data"}, safe=False)
           
        
class ProductAPI(APIView):
    def post(self, request):
        Serializer = ProductSerializer(data=request.data)
        if Product.objects.filter(**request.data).exists():
            raise serializers.ValidationError("category already exist")
        if Serializer.is_valid():
            Serializer.save()
            return JsonResponse({"msg":"data added successfully"},safe=False)
        else:
            return JsonResponse({"msg":"invalid data "},safe=False)
        
    
    
    def delete(self, request, pk):
        item = Product.objects.filter(id=pk)
        item.delete()
        return JsonResponse({"msg":"delete"},safe=False)

    def put(self, request,pk):
        item = Product.objects.get(pk=pk)
        Serializer = ProductSerializer(instance=item, data=request.data)
        if Product.objects.filter(**request.data).exists():
            raise serializers.ValidationError("category of this name already exists")

        if Serializer.is_valid():
            Serializer.save()
            return JsonResponse({"msg":"category updated"},safe=False)
        else:
            return JsonResponse({"msg":"invalid form data"}, safe=False)

class ProductlistAPI(APIView):
    def get(self, request):
        item = Product.objects.all()
        Serializer = ProductSerializer(item, many=True)
        data = Serializer.data
        print(data,1111111111111111111111111)
        return render(request, 'Product/all_product.html',{"get_data":data})
        # return JsonResponse(Serializer.data,safe=False)
        