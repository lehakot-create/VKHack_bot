# Generated by Django 4.2 on 2023-04-06 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_employee_department_employee_mentor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='date_time_contract',
            field=models.DateField(verbose_name='Дата подписания трудового контракта'),
        ),
    ]
