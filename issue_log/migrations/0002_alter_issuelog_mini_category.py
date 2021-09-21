# Generated by Django 3.2.4 on 2021-09-21 09:33

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_alter_minicategory_name'),
        ('issue_log', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuelog',
            name='mini_category',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='sub_category', chained_model_field='sub_category', null=True, on_delete=django.db.models.deletion.CASCADE, to='category.minicategory'),
        ),
    ]
