from django.db import models
from django.urls import reverse
from datetime import datetime, date



# Create your models here.


class EquipmentType(models.Model):
    name = models.CharField('Equipment Type', max_length=30)
    created_at = models.DateTimeField(
        'Joined', auto_now=True, auto_now_add=False)
    last_modified = models.DateTimeField(auto_now=False, auto_now_add=True)


    def __str__(self):
        return "{}".format(self.name[:25])

    class Meta:
        verbose_name = "Equipment Type"
        verbose_name_plural = "Equipment Types"


class EquipmentMake(models.Model):
    name = models.CharField('Equipment Make', max_length=30)
    equipment_type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE)
    created_at = models.DateTimeField(
        'Joined', auto_now=True, auto_now_add=False)
    last_modified = models.DateTimeField(auto_now=False, auto_now_add=True)


    def __str__(self):
        return "{}".format(self.name[:25])

    class Meta:
        verbose_name = "Equipment Make"
        verbose_name_plural = "Equipment Make"



class EquipmentBrand(models.Model):
    name = models.CharField('Equipment Brand', max_length=30)
    equipment_make = models.ForeignKey(EquipmentMake, on_delete=models.CASCADE)
    created_at = models.DateTimeField(
        'Joined', auto_now=True, auto_now_add=False)
    last_modified = models.DateTimeField(auto_now=False, auto_now_add=True)


    def __str__(self):
        return "{}".format(self.name[:25])


    class Meta:
        verbose_name = "Equipment Brand"
        verbose_name_plural = "Equipment Brands"

class EquipmentModel(models.Model):
    name = models.CharField('Equipment Model', max_length=30)
    equipment_brand = models.ForeignKey(EquipmentBrand, on_delete=models.CASCADE)
    created_at = models.DateTimeField(
        'Joined', auto_now=True, auto_now_add=False)
    last_modified = models.DateTimeField(auto_now=False, auto_now_add=True)


    def __str__(self):
        return "{}".format(self.name[:25])


    class Meta:
        verbose_name = "Equipment Model "
        verbose_name_plural = "Equipment Models"



    
