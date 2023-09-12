# Generated by Django 4.2.4 on 2023-08-19 09:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("polls", "0002_alter_laptopmodels_table"),
    ]

    operations = [
        migrations.CreateModel(
            name="Choice",
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
                ("choice_text", models.CharField(max_length=200)),
                ("votes", models.IntegerField(default=0)),
            ],
            options={
                "db_table": "polls_choice",
            },
        ),
        migrations.CreateModel(
            name="Question",
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
                ("question_text", models.CharField(default="", max_length=200)),
                ("pub_date", models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                "db_table": "polls_question",
            },
        ),
        migrations.DeleteModel(
            name="LaptopModels",
        ),
        migrations.AddField(
            model_name="choice",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="polls.question"
            ),
        ),
    ]