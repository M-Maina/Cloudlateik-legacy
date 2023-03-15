from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Customer
from django.db.models import Q

# Create your views here.


def index(request):
    customer = Customer.objects.filter(Customer.email)
    print(customer)
    
    #To obtain greater than in queries eg price__gt=20, price__lt=20, price__eq=20
    
    #product = Customer.objects.filter(pk=0).first() #This returns None
    #exists = Customer.objects.filter(pk=0).exists()
    # #query_set = Product.objects.all() #gets all the objects from a given table 
    # try:
    #     product = Customer.objects.get(pk=0) # django refers to that object/item alone
    # except ObjectDoesNotExist:
    #     pass
    
    #product = Customer.objects.filter(inventory__lt=10).filter(unit_price__lt=20)
    #product = Customer.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))
    
    
    
    # for product in query_set:
    #     print(product)
    return render(request, 'playground/hello.htm', {'customers':list(customer)})