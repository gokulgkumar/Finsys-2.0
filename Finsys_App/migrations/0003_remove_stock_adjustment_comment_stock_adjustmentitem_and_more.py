# Generated by Django 4.2.3 on 2024-02-26 08:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Finsys_App', '0002_remove_stock_reason_stock_adjustment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock_adjustment_comment',
            name='stock_adjustmentitem',
        ),
        migrations.AlterField(
            model_name='employee_comment',
            name='date',
            field=models.DateField(default=datetime.date(2024, 2, 26)),
        ),
        migrations.AlterField(
            model_name='holiday_comment',
            name='date',
            field=models.DateField(default=datetime.date(2024, 2, 26)),
        ),
    ]
