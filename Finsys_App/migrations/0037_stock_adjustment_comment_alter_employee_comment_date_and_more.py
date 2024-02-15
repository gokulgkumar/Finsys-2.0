# Generated by Django 4.2.3 on 2024-02-15 15:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Finsys_App', '0036_stock_adjustment_items_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock_adjustment',
            name='comment',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='employee_comment',
            name='date',
            field=models.DateField(default=datetime.date(2024, 2, 15)),
        ),
        migrations.AlterField(
            model_name='holiday_comment',
            name='date',
            field=models.DateField(default=datetime.date(2024, 2, 15)),
        ),
    ]
