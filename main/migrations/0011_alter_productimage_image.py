# Generated by Django 5.0.4 on 2024-04-23 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_productimage_banner_alter_productimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(default='media/Product/i_phone.webp', upload_to='Product'),
        ),
    ]
