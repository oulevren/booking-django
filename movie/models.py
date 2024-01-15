from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.text import slugify
from django.utils import timezone


# Create your models here.

class Otel(models.Model):
    username=models.CharField
    title = models.CharField(max_length=50)
    adres = models.CharField(max_length=100,default='bir adres')
    image = models.ImageField(upload_to='tesis_images',null=True)
    rating = models.CharField(max_length=5)
    map = models.CharField(max_length=10000)
    review_count = models.IntegerField()
    price = models.CharField(max_length=20)
    tax = models.CharField(max_length=50)
    cancel = models.CharField(max_length=25)
    room = models.CharField(max_length=500)
    is_active = models.BooleanField()
    created_at = models.DateTimeField(default=timezone.now) 
    # category = models.ForeignKey(category,on_delete=models.CASCADE) #*birtane kategori bilgisi alır.
    # category = models.ManyToManyField(category) #*2 ve fazla farklı kategoriye aynı filmi ekleyebiliriz
    # category = models.OneToOneField(category,on_delete=models.CASCADE) #* 1 kategoriye eklenne başka kategoriye eklenemez

    def save(self,*args,**kwargs):
        self.slug= slugify(self.title)
        super().save(*args,**kwargs)


    def __str__(self):
        return self.title
    
class Tesis(models.Model):
    title = models.CharField(max_length=50)
    image = models.FileField(upload_to='hotels_images',null=True)
    adress = models.CharField(max_length=50)
    review_count = models.CharField(max_length=50)
    rating = models.CharField(max_length=5)
    price = models.CharField(max_length=10)
    is_active = models.BooleanField()
    created_at = models.DateTimeField(default=timezone.now) 

    def save(self,*args,**kwargs):
        self.slug= slugify(self.title)
        super().save(*args,**kwargs)


    def __str__(self):
        return self.title
