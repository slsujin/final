# Generated by Django 4.2.3 on 2023-08-01 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalproapp1', '0004_alter_store_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]