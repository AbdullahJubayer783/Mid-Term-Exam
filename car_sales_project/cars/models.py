from django.db import models
from brand.models import brands
# Create your models here.

class Car(models.Model):
    image = models.ImageField(upload_to ='cars/media/uploads/',blank=True, null=True)
    name = models.CharField(max_length=300)
    price = models.CharField(max_length=100,blank=True, null=True)
    quantity = models.IntegerField()
    descriptions = models.TextField()
    brand = models.ForeignKey(brands, on_delete = models.CASCADE)

    def __str__(self) :
        return self.name

class Comment(models.Model):
    post = models.ForeignKey(Car,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"Comment By {self.name}"