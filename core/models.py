from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=255)


    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return str(self.name)

class Item(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    discription = models.TextField(null=True,blank=True)
    created_by = models.DateTimeField(auto_now_add=True)
    updated_by = models.DateTimeField(auto_now=True)
    price = models.FloatField(null=True,blank=True,default=0.00)
    image = models.ImageField(default='pics.jpg',upload_to='images',null=True,blank=True)


    class Meta:
        ordering = ['-created_by','updated_by']

    def __str__(self):
        return str(self.name)
    



class Comment(models.Model):
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    comment = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.bio[0:10]

#     def 