# Generated by Django 4.2.4 on 2023-08-19 09:19

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="LaptopModels",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(default="mac", max_length=25)),
                ("price", models.PositiveIntegerField(default=1)),
                ("ram", models.PositiveSmallIntegerField(default=1)),
            ],
        ),
    ]
