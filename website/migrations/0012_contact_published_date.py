# Generated by Django 4.2.2 on 2024-10-23 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0011_alter_contact_created_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="published_date",
            field=models.DateTimeField(null=True),
        ),
    ]
