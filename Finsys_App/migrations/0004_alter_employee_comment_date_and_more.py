# Generated by Django 4.2.3 on 2024-03-01 09:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Finsys_App', '0003_remove_stock_adjustment_comment_stock_adjustmentitem_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_comment',
            name='date',
            field=models.DateField(default=datetime.date(2024, 3, 1)),
        ),
        migrations.AlterField(
            model_name='holiday_comment',
            name='date',
            field=models.DateField(default=datetime.date(2024, 3, 1)),
        ),
    ]
