# Generated by Django 4.2.5 on 2023-11-26 10:53

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0007_alter_purchase_options_alter_userprofile_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="purchase",
            options={"verbose_name": "объект", "verbose_name_plural": "Покупки"},
        ),
    ]
