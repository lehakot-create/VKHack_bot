# Generated by Django 4.2 on 2023-04-06 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_employee_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='uuid',
            field=models.CharField(max_length=64, null=True),
        ),
    ]