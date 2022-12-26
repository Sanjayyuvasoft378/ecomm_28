from django.db import models



CATEGORY_CHOICE = (
    ("CR","Curd"),
    ("ML","Milk"),
    ("LS","Lassi"),
    ("MS","Milkshake"),
    ("PN","Paneer"),
    ("GH","Ghee"),
    ("CZ","Cheese"),
    ("IC","Ice Creames"),
    ("BM","Buttermilk")
    
)
    

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discount_price = models.FloatField()
    description = models.TextField(max_length=200)
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICE, max_length=2)
    product_image = models.ImageField(upload_to="product")
    def __str__(self):
        return self.title
    
class UserRegistration(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    password1 = models.CharField(max_length=15)
    password2 = models.CharField(max_length=15)

    def __str__(self):
        return self.username
    
    
class ContactUs(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    subject = models.CharField(max_length=200)
    your_message = models.TextField(max_length=200)
    
    def __str__(self):
        return self.your_message


    
