# Generated by Django 4.2.5 on 2023-11-18 09:40

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0003_purchase_creating_time"),
    ]

    operations = [
        migrations.RenameField(
            model_name="purchase",
            old_name="creating_time",
            new_name="creation_time",
        ),
    ]
