# Generated by Django 4.2.3 on 2023-08-01 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalproapp1', '0007_alter_store_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='purpose',
            field=models.CharField(choices=[('enquiry', 'enquiry'), ('place order', 'place order'), ('return', 'return'), ('rating', 'rating')], max_length=20),
        ),
    ]