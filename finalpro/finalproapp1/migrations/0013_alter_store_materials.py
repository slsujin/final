# Generated by Django 4.2.3 on 2023-08-03 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalproapp1', '0012_store_materials'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='materials',
            field=models.TextField(default=None, max_length=100),
        ),
    ]
