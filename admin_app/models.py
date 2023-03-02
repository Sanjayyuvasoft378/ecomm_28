from django.db import models

class MainCategory(models.Model):
    category_name = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    cate_image = models.ImageField(upload_to='media/',max_length=255)
    def __str__(self):
        return self.category_name

class SubCategory(models.Model):
    main_category_id = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='subcategory')

    def __str__(self):
        return self.category_name

class ChildCategory(models.Model):
    main_category_id = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    sub_category_id = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='subcategory')

    def __str__(self):
        return self.category_name

class Product(models.Model):
    main_category_id = models.ForeignKey(MainCategory,on_delete=models.CASCADE)
    sub_category_id = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=20)
    price = models.FloatField()
    qty = models.IntegerField()
    image = models.ImageField(upload_to='product/')
    description = models.TextField()

class Coupons(models.Model):
    coupon_type = models.CharField(max_length=20)
    amount = models.FloatField(max_length=20)
    used = models.CharField(max_length=20)

class Staff(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    mobile_no = models.CharField(max_length=10)
    gender = models.CharField(max_length=20)

    # def __str__(self):
    #     return self.first_name
    
class Posts(models.Model):
    image = models.ImageField(upload_to='Posts')
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title
    
class Slider(models.Model):
    image = models.ImageField(upload_to='slider_image/')
    heading = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.heading
    

    