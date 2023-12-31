# Generated by Django 4.2.5 on 2023-11-18 09:49

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0006_alter_event_table_alter_ticket_table"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="event",
            options={"verbose_name": "событие", "verbose_name_plural": "События"},
        ),
        migrations.AlterModelOptions(
            name="ticket",
            options={"verbose_name": "билет", "verbose_name_plural": "Билеты"},
        ),
        migrations.AlterModelTable(
            name="event",
            table="events",
        ),
        migrations.AlterModelTable(
            name="ticket",
            table=None,
        ),
    ]
