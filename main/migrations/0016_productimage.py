# Generated by Django 5.0.4 on 2024-04-23 13:54

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_delete_productimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(default='Product/i_phone.webp', upload_to='Product')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Product_image', to='main.product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
