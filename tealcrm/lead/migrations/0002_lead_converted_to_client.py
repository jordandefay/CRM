# Generated by Django 4.2.5 on 2023-10-09 06:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lead", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="lead",
            name="converted_to_client",
            field=models.BooleanField(default=False),
        ),
    ]
