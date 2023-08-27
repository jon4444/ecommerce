# Generated by Django 4.2.1 on 2023-08-10 10:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0006_alter_category_id_alter_product_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductSpecification",
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
                (
                    "name",
                    models.CharField(
                        help_text="Required", max_length=255, verbose_name="Name"
                    ),
                ),
            ],
            options={
                "verbose_name": "Product Specification",
                "verbose_name_plural": "Product Specifications",
            },
        ),
        migrations.CreateModel(
            name="ProductType",
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
                (
                    "name",
                    models.CharField(
                        help_text="Required",
                        max_length=255,
                        unique=True,
                        verbose_name="Product Name",
                    ),
                ),
            ],
            options={
                "verbose_name": "Product Type",
                "verbose_name_plural": "Product Types",
            },
        ),
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "Category", "verbose_name_plural": "Categories"},
        ),
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ("-created_at",),
                "verbose_name": "Product",
                "verbose_name_plural": "Products",
            },
        ),
        migrations.RemoveField(model_name="product", name="author",),
        migrations.RemoveField(model_name="product", name="created",),
        migrations.RemoveField(model_name="product", name="created_by",),
        migrations.RemoveField(model_name="product", name="image",),
        migrations.RemoveField(model_name="product", name="in_stock",),
        migrations.RemoveField(model_name="product", name="price",),
        migrations.RemoveField(model_name="product", name="updated",),
        migrations.AddField(
            model_name="category",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="category",
            name="level",
            field=models.PositiveIntegerField(default=0, verbose_name="Level"),
        ),
        migrations.AddField(
            model_name="category",
            name="lft",
            field=models.PositiveIntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="category",
            name="parent",
            field=mptt.fields.TreeForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="children",
                to="store.category",
            ),
        ),
        migrations.AddField(
            model_name="category",
            name="rght",
            field=models.PositiveIntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="category",
            name="tree_id",
            field=models.PositiveIntegerField(db_index=True, default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="product",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Created at",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="product",
            name="discount_price",
            field=models.DecimalField(
                decimal_places=2,
                default=0,
                error_messages={
                    "name": {"max_length": "The price must be between 0 and 999.99."}
                },
                help_text="Maximum 999.99",
                max_digits=5,
                verbose_name="Discount Price",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="product",
            name="regular_price",
            field=models.DecimalField(
                decimal_places=2,
                default=0,
                error_messages={
                    "name": {"max_length": "The price must be between 0 and 999.99."}
                },
                help_text="Maximum 999.99",
                max_digits=5,
                verbose_name="Regular Price",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="product",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="Updated at"),
        ),
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(
                help_text="Required and unique",
                max_length=255,
                unique=True,
                verbose_name="Category Name",
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(
                max_length=255, null=True, unique=True, verbose_name="Category safe URL"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.RESTRICT, to="store.category"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(
                blank=True, help_text="Not Required", verbose_name="description"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="is_active",
            field=models.BooleanField(
                default=True,
                help_text="Change product visibility",
                verbose_name="Product visibility",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="title",
            field=models.CharField(
                help_text="Required", max_length=255, verbose_name="title"
            ),
        ),
        migrations.CreateModel(
            name="ProductSpecificationValue",
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
                (
                    "value",
                    models.CharField(
                        help_text="Product specification value maximum of 255 words",
                        max_length=255,
                        verbose_name="value",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="store.product"
                    ),
                ),
                (
                    "specification",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="store.productspecification",
                    ),
                ),
            ],
            options={
                "verbose_name": "Product Specification Value",
                "verbose_name_plural": "Product Specification Values",
            },
        ),
        migrations.AddField(
            model_name="productspecification",
            name="product_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.RESTRICT, to="store.producttype"
            ),
        ),
        migrations.CreateModel(
            name="ProductImage",
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
                (
                    "image",
                    models.ImageField(
                        default="images/default.png",
                        help_text="Upload a product image",
                        upload_to="images/",
                        verbose_name="image",
                    ),
                ),
                (
                    "alt_text",
                    models.CharField(
                        blank=True,
                        help_text="Please dd alternative text",
                        max_length=255,
                        null=True,
                        verbose_name="Alternative Text",
                    ),
                ),
                ("is_feature", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product_image",
                        to="store.product",
                    ),
                ),
            ],
            options={
                "verbose_name": "Product Image",
                "verbose_name_plural": "Product Images",
            },
        ),
        migrations.AddField(
            model_name="product",
            name="product_type",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.RESTRICT,
                to="store.producttype",
            ),
            preserve_default=False,
        ),
    ]