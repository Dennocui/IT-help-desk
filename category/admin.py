from django.contrib import admin

# Register your models here.


from .models import Category, SubCategory, MiniCategory

admin.site.register(Category)

@ admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    # resource_class = IssueLogResource
    list_display = ('category', 'name')

    fieldsets = (
        ('Basic Information', {
           
            'fields': (
                ('category', 'name') 
                       )}),

    )

@ admin.register(MiniCategory)
class MiniCategoryAdmin(admin.ModelAdmin):
    # resource_class = IssueLogResource
    list_display = ('sub_category','name')

    fieldsets = (
        ('Basic Information', {
           
            'fields': (
                ('sub_category','name') 
                       )}),

    )