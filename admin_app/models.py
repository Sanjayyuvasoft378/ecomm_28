from django.db import models

class MainCategory(models.Model):
    category_name = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media')
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
    price = models.IntegerField()
    qty = models.IntegerField()
    image = models.ImageField(upload_to='product')
    description = models.TextField()
    

