from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Customer
from django.db.models import Q, F, Func, Count, ExpressionWrapper
from django.db.models import Value
from django.db.models.functions import Concat
from django.db.models.aggregates import Count, Max, Min, Avg

from django.contrib.contenttypes.models import ContentType
from store.models import Product, Collection
from tags.models import TaggedItem

# Create your views here.


#def index(request):
    #queryset = Customer.objects.aggregate(count=Count('id'))
    #customer = Customer.objects.filter(Customer.email)
    
    #To obtain greater than in queries eg price__gt=20, price__lt=20, price__eq=20
    
    #product = Customer.objects.filter(pk=0).first() #This returns None
    #exists = Customer.objects.filter(pk=0).exists()
    # #query_set = Product.objects.all() #gets all the objects from a given table 
    # try:
    #     product = Customer.objects.get(pk=0) # django refers to that object/item alone
    # except ObjectDoesNotExist:
    #     pass
    
    #product = Customer.objects.filter(inventory__lt=10).filter(unit_price__lt=20)
    
    #product = Customer.objects.filter(first_name=F('email'))
    
    #product = Customer.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))
    
    
    
    #customer = Customer.objects.order_by('email')
    
    #customer = Customer.objects.earliest('phone')
    
    #queryset = Customer.objects.all()[:25]
    
    #queryset = Customer.objects.values('id', 'first_name')[:25]
    
    #queryset = Customer.objects.only('id', 'last_name')[:25]
    
    #queryset =Product.objects.select_related('promotions').select_related('collection').all()
    #{{ product.collection.title }}
    
    #queryset = Customer.objects.prefetch_related('collection').all()
    
    #queryset = Customer.objects.select_related('collection__someOtherField').all()
    
    #queryset = Order.objects.select_related('Customer').order_by('-placed_at')[:5]
    
    #{{ order.id }}  - {{ order.customer.first_name }}
    
    #queryset = Order.objects.select_related('Customer').prefetch_related('').order_by('-placed_at')[:5]
    
    # for product in query_set:
    #     print(product)
    
     
    #return render(request, 'playground/hello.htm', {'customers': queryset })
    
    
def index(request):
    #queryset = Customer.objects.annotate(is_new=Value(True))# we create a new field in the database is_new
   # queryset = Customer.objects.annotate(new_id=F('id') + 1)
    # queryset = Customer.objects.annotate(
    #     #concatinate
    #     full_name = Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT')
    # )
    
    # queryset = Customer.objects.annotate(
    #     #concatinate
    #     full_name = Concat('first_name', Value(' '), 'last_name')
    # )
    
    # queryset = Customer.objects.annotate(
    #     orders_count=Count('order'))
    
    # discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
    # queryset = Customer.objects.annotate(
    #     dicounted_price=discounted_price
    # )
    
    # content_type = ContentType.objects.get_for_model(Product)
    # queryset = TaggedItem.objects.selected_related('tag').filter(
    #     content_type=content_type,
    #     object_id=1
    # )
    
    
    # collection = Collection()
    # collection.title = 'Video Games'
    # collection.featured_product = Product(pk=1)
    # collection.save()
    #collection.featured_product_id = 1
    return render(request, 'playground/hello.htm')