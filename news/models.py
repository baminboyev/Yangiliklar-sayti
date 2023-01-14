from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Region(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class New(models.Model):
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    region = models.ForeignKey(Region, on_delete= models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=150)
    summary = models.CharField(max_length=300)
    body = models.TextField()
    image = models.ImageField(upload_to= 'images/')
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
