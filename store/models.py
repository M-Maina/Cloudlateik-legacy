from django.db import models

# Create your models here.


class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()
    
    
class Collection(models.Model):
    title = models.CharField(max_length=255) #Product in"Product" resolves circular dependencies"
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+')
    #Fixing related name asssociated Errors
    

class Product(models.Model):
      title = models.CharField(max_length=255)
      slug = models.SlugField(null=True)
      description = models.TextField()
      price = models.DecimalField(max_digits=6, decimal_places=2)
      inventory = models.IntegerField()
      last_update = models.DateTimeField(auto_now=True)
      collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
      promotions = models.ManyToManyField(Promotion)
      
       
class Customer(models.Model):
     MEMBERSHIP_BRONZE = 'B'
     MEMBERSHIP_SILVER = 'S'
     MEMBERSHIP_GOLD = 'G'
     
     MEMBERSHIP_CHOICES = [
         (MEMBERSHIP_BRONZE, 'Bronze'),
         (MEMBERSHIP_SILVER , 'Silver'),
         (MEMBERSHIP_GOLD , 'Gold'),
     ]
     
     given_name = models.CharField(max_length=255)
     last_name = models.CharField(max_length=255)
     email = models.EmailField(unique=True)
     phone = models.CharField(max_length=255)
     birth_date = models.DateField(null=True)
     membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)
     

class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING,'Pending'),
        (PAYMENT_STATUS_COMPLETE,'Complete'),
        (PAYMENT_STATUS_FAILED,'Failed'),
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES, default= PAYMENT_STATUS_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT) #ORDER SHOULD NEVER BE DELETED
    
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    
    
class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)#PK allows don't allow duplicate values
    
    
class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart(), on_delete=models.CASCADE)
    prouct = models.ForeignKey(Product(), on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
    
    
    
    