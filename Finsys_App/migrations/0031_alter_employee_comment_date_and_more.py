# Generated by Django 5.0.1 on 2024-02-02 07:14

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Finsys_App', '0030_alter_employee_comment_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_comment',
            name='date',
            field=models.DateField(default=datetime.date(2024, 2, 2)),
        ),
        migrations.AlterField(
            model_name='holiday_comment',
            name='date',
            field=models.DateField(default=datetime.date(2024, 2, 2)),
        ),
        migrations.CreateModel(
            name='Fin_CompanyRepeatEvery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repeat_every', models.CharField(blank=True, max_length=100, null=True)),
                ('repeat_type', models.CharField(blank=True, max_length=100, null=True)),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('days', models.IntegerField(blank=True, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_company_details')),
            ],
        ),
    ]
