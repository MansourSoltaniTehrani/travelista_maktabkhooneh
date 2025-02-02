# Generated by Django 4.2.2 on 2024-10-29 14:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name": "category",
                "verbose_name_plural": "categories",
                "ordering": ("name",),
            },
        ),
        migrations.AlterModelOptions(
            name="post",
            options={
                "ordering": ("-created_date",),
                "verbose_name": "post",
                "verbose_name_plural": "postsss",
            },
        ),
        migrations.AddField(
            model_name="post",
            name="author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="image",
            field=models.ImageField(default="blog/default.jpg", upload_to="blog/"),
        ),
        migrations.AddField(
            model_name="post",
            name="category",
            field=models.ManyToManyField(to="blog.category"),
        ),
    ]
