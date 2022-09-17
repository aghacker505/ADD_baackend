# Generated by Django 4.1 on 2022-09-16 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("category", models.CharField(max_length=150)),
                ("title", models.CharField(max_length=100)),
                ("price", models.CharField(max_length=13)),
                ("image", models.URLField()),
                ("discount", models.CharField(max_length=20)),
                ("description", models.TextField()),
                ("status", models.BooleanField()),
                ("date_created", models.DateField(auto_now_add=True)),
                ("unique_id", models.CharField(max_length=100)),
            ],
            options={"ordering": ["-date_created"],},
        ),
    ]
