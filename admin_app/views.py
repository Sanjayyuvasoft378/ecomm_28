from django.shortcuts import render,redirect

from PIL import Image
from io import BytesIO
import base64
    
from .models import *
import random
from .serializers import *
from Ecomm_app.serializers import UserRegistrationSerializer, ProductReviewSerializer, ProductCommentSerializer,ChangePasswordSerializer
from Ecomm_app.models import UserRegistration,ProductReviewModel,ProductCommentModel
from rest_framework.views import APIView
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

def editprofile(request):
    return render(request, 'Account/edit_profile.html')

def changepassword(request):
    return render(request, 'Account/change_password.html')

def allproductlist(request):
    return render(request, 'Product/all_product.html')

@login_required
def dashboard(request):
    return render(request,'dashboard.html')


def login(request):
    return render(request,'Account/login.html')

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
    return render(request,'coupons/coupons.html')

    
# Convert Image to Base64
def image_to_base64(image):
    buff = BytesIO()
    image.save(buff, format="PNG")
    img_str = base64.b64encode(buff.getvalue())
    img_str = img_str.decode("utf-8")  # convert to str and cut b'' chars
    return img_str


class CustomerListAPI(APIView):
    def get(self, request):
        customer = UserRegistration.objects.all()
        a = customer.count()
        Serializer = UserRegistrationSerializer(customer,many=True)
        data = Serializer.data
        return render(request, 'customer_list.html',{"data":data})
        # return JsonResponse(Serializer.data, safe=False)

# Create your views here.
class MainCategoryAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            image = Image.open("/home/karunasakle/Pictures/Screenshot from 2022-06-29 14-13-05.png")      
            Serializer = MaincategorySerializer(data=data)  
            import pdb ; pdb.set_trace()
            if MainCategory.objects.filter(**request.data).exists():
                raise serializers.ValidationError("category already exist")
            if Serializer.is_valid():
                image64 = image_to_base64(image)
                Serializer.save()
                # return render(request, 'Categories/Main-Category/main_category_list.html',{'image64': image64})
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
            return JsonResponse({"msg":"invalid data "},safe=False,status=400)
        
    def get(self, request):
        item = Product.objects.all()
        Serializer = ProductSerializer(item, many=True)
        data = Serializer.data
        # return render(request,'Product/all_product.html',{"data":data})
        return JsonResponse(Serializer.data, safe=False)
    
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
    
class ProductDeactivateAPI(APIView):
    def get(self, request):
        try:
            if status==0:
                item = Product.objects.all()
                Serializer = ProductSerializer(item,many=True)
                return JsonResponse(Serializer.data,safe=False,status=200)
            elif status==1:
                item = Product.objects.filter(status="deactivated")
                Serializer = ProductSerializer(item)
                return JsonResponse(Serializer.data,safe=False,status=200)
            elif status==2:
                item = Product.objects.filter(status="activated")
                Serializer = ProductSerializer(item)
                return JsonResponse(Serializer.data,safe=False,status=200)
            else:
                return JsonResponse(Serializer.error,safe=False,status=400)
        except Exception as e:
            return JsonResponse({"msg":"Internal server error {}".format(e)},safe=False,status=500)
        
class CouponsAPI(APIView):
    def post(self, request):
        Serializer = CouponsSerializer(data=request.data)
        if Coupons.objects.filter(**request.data).exists():
            raise serializers.ValidationError("category already exist")
        if Serializer.is_valid():
            Serializer.save()
            return redirect('/api/v1/coupons/')
            # return JsonResponse({"msg":"da    ta added successfully"},safe=False)
        else:
            return JsonResponse({"msg":"invalid data "},safe=False)
        
    def get(self, request):
        item = Coupons.objects.all()
        Serializer = CouponsSerializer(item, many=True)
        data= Serializer.data
        return render(request,'coupons/coupons.html',{"data":data})
        return JsonResponse(Serializer.data, safe=False)
    
    def delete(self, request, pk):
        item = Coupons.objects.filter(id=pk)
        item.delete()
        return render(request, "coupons/coupons.html")
        # return JsonResponse({"msg":"delete"},safe=False)

    def put(self, request,pk):
        item = Coupons.objects.get(pk=pk)
        Serializer = CouponsSerializer(instance=item, data=request.data)
        if Coupons.objects.filter(**request.data).exists():
            raise serializers.ValidationError("category of this name already exists")
        if Serializer.is_valid():
            Serializer.save()
            return render(request, "coupons/coupons.html")
            # return JsonResponse({"msg":"category updated"},safe=False)
        else:
            return JsonResponse({"msg":"invalid form data"}, safe=False)

class StaffAPI(APIView):
    def post(self, request):
        try:
            Serializer = StaffSerializer(data=request.data)
            if Staff.objects.filter(**request.data).exists():
                raise serializers.ValidationError("already exists")
            if Serializer.is_valid(raise_exception=True):
                Serializer.save() 
                return redirect('/api/v1/staff/')
                # return JsonResponse({"msg":"data added successfully"},safe=False,status=200)
            else:
                return render(request, "staff_list.html")
                # return JsonResponse({"msg":"Invalid input"},safe=False)
        except Exception as e:
            return JsonResponse({"msg":"Internal server error {}".format(e)},safe=False,status=500)
        
    def get(self, request):
        try:
            item = Staff.objects.all()
            Serializer = StaffSerializer(item, many=True)        
            data = Serializer.data
            return render(request, 'staff_list.html',{"data":data})
            # return JsonResponse(Serializer.data,safe=False)
        except Exception as e:
            return JsonResponse({"msg":"Internal server eror {}".format(e)},safe=False, status=500)

    def delete(self, request, id):
        print("333333333",type(id))
        item = Staff.objects.filter(id=id)
        item.delete()
        return JsonResponse({"msg":"data deleted successfully"},safe=False, status=200)

    def put(self, request, pk):
        item = Staff.objects.get(pk=pk)
        Serializer = StaffSerializer(instance=item, data=request.data)
        if Staff.objects.filter(**request.data).exists():
            raise serializers.ValidationError("already exist")
        if Serializer.is_valid():
            Serializer.save()
            return JsonResponse({"msg":"data updated successfully"},safe=False,status=200)
        else:
            return JsonResponse({"msg":"Invalid data"},safe=False,status=500)

class PostsAPI(APIView):
    def post(self, request):
        try:
            Serializer = PostsSerializer(data=request.data , instance=request.user)
            if Posts.objects.filter(**request.data).exists():
                raise serializers.ValidationError("already exists")
            if Serializer.is_valid(raise_exception=True):
                Serializer.save() 
                return JsonResponse({"msg":"data added successfully"},safe=False,status=200)
            else:
                return JsonResponse({"msg":"Invalid input"},safe=False)
        except Exception as e:
            return JsonResponse({"msg":"Internal server error {}".format(e)},safe=False,status=500)
        
    def get(self, request):
        try:
            item = Posts.objects.all()
            Serializer = PostsSerializer(item, many=True)        
            data = Serializer.data
            a = data.count

            return render(request,'Blog/posts_list.html',{"data":data,"a":a})
            # return JsonResponse(Serializer.data,safe=False)
        except Exception as e:
            return JsonResponse({"msg":"Internal server eror {}".format(e)},safe=False, status=500)

    def delete(self, request, pk):
        item = Posts.objects.filter(id=pk)
        item.delete()
        return JsonResponse({"msg":"data deleted successfully"},safe=False, status=200)

    def put(self, request, pk):
        item = Posts.objects.get(pk=pk)
        Serializer = PostsSerializer(instance=item, data=request.data)
        if Posts.objects.filter(**request.data).exists():
            raise serializers.ValidationError("already exist")
        if Serializer.is_valid():
            Serializer.save()
            return JsonResponse({"msg":"data updated successfully"},safe=False,status=200)
        else:
            return JsonResponse({"msg":"Invalid data"},safe=False,status=500)
         
         
class ProductReportsListAPI(APIView):
    def get(self, request):
        item = ProductCommentModel.objects.all()
        Serializer = ProductCommentSerializer(item, many=True)
        data = Serializer.data
        return render(request, 'Product/product_report.html',{"data":data})


class ProductReviewListAPI(APIView):
    def get(self, request):
        item = ProductReviewModel.objects.all()
        Serializer = ProductReviewSerializer(item, many=True)
        data = Serializer.data
        # return JsonResponse(Serializer.data,safe=False,status=200)
        return render(request, 'Product/product_reviews.html',{"data":data})
    
class ProductCommentListAPI(APIView):
    def get(self, request):
        item = ProductCommentModel.objects.all()
        Serializer = ProductCommentSerializer(item, many=True)
        data = Serializer.data
        # return JsonResponse(Serializer.data,safe=False,status=200)
        return render(request, 'Product/product_comments.html',{"data":data})

class ChangePasswordAPI(APIView):
    def post(self, request):
        Serializer = ChangePasswordSerializer(data=request.data, context={"user":request.user})
        if Serializer.is_valid(raise_exception=True):
            Serializer.save()
            return redirect('home/')
        else:
            return render(request,'app/changepasword.html')
        
class DeactivateProductAPI(APIView):
    def get(self, request):
        try:
            item = Product.objects.find(status=False)
            Serializer = ProductSerializer(item)
            data = Serializer.data
            return render(request,'Product/deactivate_product.html',{"data":data})
        except Exception as e:
            return JsonResponse({"msg":"Internal server error {}".format(e)},safe=False,status=500)
        
class PopularProductAPI(APIView):
    def get(self, request):
        item = Product.objects.all()
        Serializer = ProductSerializer(item, many=True)
        data = Serializer.data
        return render(request, 'Product/popular_product.html',{"data":data})
        # return JsonResponse(data,safe=False,status=200)
    
    
class SliderAPI(APIView):
    def post(self, request):
        Serializer = SliderSerializer(data = request.data)
        if Slider.objects.filter(**request.data).exists():
            raise serializers.ValidationError("heading already exists")
        if Serializer.is_valid():
            Serializer.save()
            return JsonResponse({"msg":"data added successfully"},safe=False,status=200)
        else:
            return JsonResponse({"msg":"Invlid form data"},safe=False,status=400)

    def get(self, request):
        item = Slider.objects.all()
        Serializer = SliderSerializer(item, many=True)
        data = Serializer.data
        return render(request,'slider.html',{"data":data})

    def delete(self, request,pk):
        item = Slider.objects.filter(id=pk)
        item.delete()
        return JsonResponse({"msg":"data deleted "},safe=False,status=200)

    def put(self, request, pk):
        item = Slider.objects.get(id=pk)
        Serializer = SliderSerializer(data = request.data, instance=item)
        if Slider.objects.filter(**request.data).exists():
            raise serializers.ValidationError("heading already exists")
        if Serializer.is_valid():
            Serializer.save()
            return JsonResponse({"msg":"data added successfully"},safe=False,status=200)
        else:
            return JsonResponse({"msg":"Invlid form data"},safe=False,status=400)

        


        