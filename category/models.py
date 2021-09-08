from django.db import models
from django.urls import reverse
from datetime import datetime, date



# Create your models here.


class Category(models.Model):
    name = models.CharField('Category', max_length=30)
    created_at = models.DateTimeField(
        'Joined', auto_now=True, auto_now_add=False)
    last_modified = models.DateTimeField(auto_now=False, auto_now_add=True)


    def __str__(self):
        return "{}".format(self.name[:25])

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class SubCategory(models.Model):
    name = models.CharField('Sub-Category', max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(
        'Joined', auto_now=True, auto_now_add=False)
    last_modified = models.DateTimeField(auto_now=False, auto_now_add=True)


    def __str__(self):
        return "{}".format(self.name[:25])


    class Meta:
        verbose_name = "Sub-Category"
        verbose_name_plural = "Sub-Categories"

class MiniCategory(models.Model):
    name = models.CharField('Mini-Category', max_length=30)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(
        'Joined', auto_now=True, auto_now_add=False)
    last_modified = models.DateTimeField(auto_now=False, auto_now_add=True)


    def __str__(self):
        return "{}".format(self.name[:25])


    class Meta:
        verbose_name = "Mini-Category"
        verbose_name_plural = "Mini-Categories"



    
