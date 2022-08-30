from django.db import models
from django.urls import reverse
from datetime import datetime, date

from category.models import EquipmentType, EquipmentModel, EquipmentMake,EquipmentBrand
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.
    

class IssueLog(models.Model):
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"

    ISSUE_PRIORITY = [
        (LOW, 'LOW'),
        (MEDIUM, 'MEDIUM'),
        (HIGH, 'HIGH'),
    ]

    CLOSED = "CLOSED"
    OPEN = "OPEN"

    ISSUE_STATUS = [
        (OPEN, 'OPEN'),
        (CLOSED, 'CLOSED'),
        
    ]

    issue = models.CharField('Issue', max_length=30)
    status = models.CharField(
        max_length=6,
        choices=ISSUE_STATUS,
        default=OPEN,
    )
    priority = models.CharField(
        max_length=6,
        choices=ISSUE_PRIORITY,
        default=LOW,
    )


    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='issuelogs')
    personel_assinged = models.ForeignKey(User, on_delete=models.CASCADE)

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

    # sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    issue_date = models.DateField('Issue Date')
    due_date = models.DateField('Due Date')

    comments = models.TextField(
        'Comments', max_length=500, null=True, blank=True)

    created_at = models.DateTimeField(
        'Joined', auto_now=True, auto_now_add=False)
    last_modified = models.DateTimeField(auto_now=False, auto_now_add=True)


    def __str__(self):
        return "{}".format(self.issue[:25])

    class Meta:
        verbose_name = "Issue Log"
        verbose_name_plural = "Issue Logs"