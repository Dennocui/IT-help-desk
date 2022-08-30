from django.contrib import admin

# Register your models here.


from category.models import EquipmentType, EquipmentModel, EquipmentMake,EquipmentBrand

admin.site.register(EquipmentType)

@ admin.register(EquipmentModel)
class EquipmentTypeAdmin(admin.ModelAdmin):
    # resource_class = IssueLogResource
    list_display = ('equipment_brand', 'name')

    fieldsets = (
        ('Basic Information', {
           
            'fields': (
                ('equipment_brand', 'name') 
                       )}),

    )

@ admin.register(EquipmentMake)
class EquipmentMakeAdmin(admin.ModelAdmin):
    # resource_class = IssueLogResource
    list_display = ('equipment_type','name')

    fieldsets = (
        ('Basic Information', {
           
            'fields': (
                ('equipment_type','name') 
                       )}),

    )

@ admin.register(EquipmentBrand)
class EquipmentBrandAdmin(admin.ModelAdmin):
    # resource_class = IssueLogResource
    list_display = ('equipment_make','name')

    fieldsets = (
        ('Basic Information', {
           
            'fields': (
                ('equipment_make','name') 
                       )}),

    )