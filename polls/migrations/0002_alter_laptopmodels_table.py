# Generated by Django 4.2.4 on 2023-08-19 09:22

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="laptopmodels",
            table="polls_laptop",
        ),
    ]
