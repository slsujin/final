# Generated by Django 4.2.3 on 2023-08-03 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalproapp1', '0010_store_course_store_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='phone',
            field=models.BigIntegerField(null=True),
        ),
    ]
