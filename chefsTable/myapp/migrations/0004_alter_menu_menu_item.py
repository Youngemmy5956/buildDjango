# Generated by Django 5.0.3 on 2024-03-28 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_menucategory_delete_drinks_remove_menu_cuisine_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='menu_item',
            field=models.CharField(max_length=200),
        ),
    ]