# Generated by Django 4.1.2 on 2022-10-19 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0020_alter_category_categories_alter_product_category"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="quantity",
            new_name="stock",
        ),
        migrations.RemoveField(
            model_name="category",
            name="categories",
        ),
        migrations.AddField(
            model_name="category",
            name="category1",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="category",
            name="category2",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="category",
            name="category3",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="category",
            name="category4",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="category",
            name="category5",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="category",
            name="category6",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
