# Generated by Django 4.2.5 on 2023-11-18 09:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0004_alter_ticket_creating_time"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ticket",
            name="creating_time",
        ),
    ]
