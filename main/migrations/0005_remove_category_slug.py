# Generated by Django 5.0.4 on 2024-04-23 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_category_category_discription_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
    ]
