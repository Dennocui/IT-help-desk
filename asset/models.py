from django.db import models

# Create your models here.
from category.models import Category,SubCategory, MiniCategory
from smart_selects.db_fields import ChainedForeignKey

class Supplier(models.Model):
    supplier_name = models.CharField('Supplier Name', max_length=200)
    phone_no = models.IntegerField('Phone Number')
    address = models.CharField('Address', max_length=200)
    email = models.CharField('Email', max_length=200)
    loation = models.CharField('Location', max_length=200)


class Asset(models.Model):
    equipment = models.ForeignKey(Category, on_delete=models.CASCADE)
    equipment_make =  ChainedForeignKey(
        SubCategory,
        chained_field="equipment",
        chained_model_field="equipment",
        show_all=False,
        auto_choose=True,
        sort=True)
    model = ChainedForeignKey(
        MiniCategory,
        chained_field="equipment_make",
        chained_model_field="equipment_make",
        show_all=False,
        auto_choose=True,
        sort=True,
        null=True,
        blank=True)

    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    serial_no =models.CharField('Serial No', max_length=30) 
    prodcut_no = models.CharField('product No', max_length=30) 
    purchase_date = models.DateField('Issue Date')
    
    purchase_price = models.DateField('Purchase Date')
    item_name  = models.CharField('Item Name', max_length=30) 
    warranty = models.IntegerField('Warranty') 
 
   
