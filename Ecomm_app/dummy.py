class AddToWishlistAPI(APIView):
    def post(self, request):
        try:
            Serializer = WishlistSerializer(data = request.data)
            if Serializer.is_valid():
                product_id = request.POST.get('product_id')
                qty = 1
                item = Wishlist(product_id=product_id,qty=qty)
                item.save()
                # messages.success(request,"data added into wishlist successfully")
                return JsonResponse({"msg":"invalid data"})
            else:
                return JsonResponse({"msg":"invalid data"})
                # messages.warning(request,"Invalid Data")
            # return render(request,'app/wishlist.html',locals())
        except Exception as e:
            return JsonResponse({"msg":"Internal server error {}".format(e)},safe=False)
            
     
     
     
     

class AddToWishlistAPI1(APIView):
    def post(self, request):
        try:
            Serializer = AddToCartSerializer(data=request.data)
            if Serializer.is_valid():
                Serializer.save()
                return JsonResponse({"msg":"Product added into wishlist"},safe=False)
            else:
                return JsonResponse({"msg":"Invalid data"},safe=False)
        except Exception as e:
            return JsonResponse({"msg":"Internal server error {}".format(e)},safe=False)



    # path('add-to-wishlist/', views.AddToWishlistAPI.as_view(), name='add-to-wishlist'),