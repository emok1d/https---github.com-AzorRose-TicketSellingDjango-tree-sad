# Generated by Django 4.2.6 on 2023-12-03 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0003_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='map_address',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='building',
            name='address',
            field=models.CharField(default='', max_length=2000),
        ),
    ]
