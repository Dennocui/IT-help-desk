from django.db import models

# Create your models here.
from category.models import EquipmentType, EquipmentModel, EquipmentMake,EquipmentBrand
from smart_selects.db_fields import ChainedForeignKey

class Supplier(models.Model):
    supplier_name = models.CharField('Supplier Name', max_length=200)
    phone_no = models.IntegerField('Phone Number')
    address = models.CharField('Address', max_length=200)
    email = models.CharField('Email', max_length=200)
    loation = models.CharField('Location', max_length=200)

    def __str__(self):
        return "{}".format(self.supplier_name[:25])



class Asset(models.Model):
    equipment_type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE)


    equipment_make =  ChainedForeignKey(
        EquipmentMake,
        chained_field="equipment_type",
        chained_model_field="equipment_type",
        show_all=False,
        auto_choose=True,
        sort=True)

    equipment_brand = ChainedForeignKey(
        EquipmentBrand,
        chained_field="equipment_make",
        chained_model_field="equipment_make",
        show_all=False,
        auto_choose=True,
        sort=True,
        null=True,
        blank=True)

    equipment_model = ChainedForeignKey(
        EquipmentModel,
        chained_field="equipment_brand",
        chained_model_field="equipment_brand",
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
    item_name  = models.CharField('Item Name', max_length=30, null=True, blank=True) 
    warranty = models.IntegerField('Warranty') 
 
   
    def __str__(self):
        return "{}".format(self.item_name[:25])
