from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.text import slugify


# Create your models here.

class Yorum(models.Model):
    description = models.CharField(max_length=100,)
    rating = models.CharField(max_length=5)
    is_active = models.BooleanField()
    # category = models.ForeignKey(category,on_delete=models.CASCADE) #*birtane kategori bilgisi alır.
    # category = models.ManyToManyField(category) #*2 ve fazla farklı kategoriye aynı filmi ekleyebiliriz
    # category = models.OneToOneField(category,on_delete=models.CASCADE) #* 1 kategoriye eklenne başka kategoriye eklenemez

    def save(self,*args,**kwargs):
        self.slug= slugify(self.description)
        super().save(*args,**kwargs)


    def __str__(self):
        return self.description