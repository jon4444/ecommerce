# Generated by Django 4.2.4 on 2023-08-06 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0005_auto_20230702_0921"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
