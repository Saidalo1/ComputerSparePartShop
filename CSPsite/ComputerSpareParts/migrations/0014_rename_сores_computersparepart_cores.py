# Generated by Django 4.1 on 2022-09-23 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ComputerSpareParts', '0013_alter_sales_computersparepart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='computersparepart',
            old_name='сores',
            new_name='cores',
        ),
    ]
