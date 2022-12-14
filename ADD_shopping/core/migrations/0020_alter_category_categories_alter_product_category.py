# Generated by Django 4.1.2 on 2022-10-19 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0019_remove_category_prdt_product_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="categories",
            field=models.CharField(
                choices=[
                    ("Winter Wear", "Winter Wear"),
                    ("Summer Wear", "Summer Wear"),
                    ("Top wear", "Top wear"),
                    ("Bottom Wear", "Bottom Wear"),
                    ("Foot wear", "Foot wear"),
                    ("Null", "Null"),
                ],
                max_length=100,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.CharField(
                choices=[
                    ("Winter Wear", "Winter Wear"),
                    ("Summer Wear", "Summer Wear"),
                    ("Top wear", "Top wear"),
                    ("Bottom Wear", "Bottom Wear"),
                    ("Foot wear", "Foot wear"),
                    ("Null", "Null"),
                ],
                max_length=200,
                null=True,
            ),
        ),
    ]
