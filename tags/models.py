from django.db import models
from django.contrib.contenttypes.models import ContentType

from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.


class Tag(models.Model):
    #What tag applied to what object
    label = models.CharField(max_length=255)
    
    
    
class TaggedItem(models.Model):
    #Type(Product,Video, Article)
    #ID
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    #Using contentType we can create Generic Relationships in our Models
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey() #Reads actual objects
    