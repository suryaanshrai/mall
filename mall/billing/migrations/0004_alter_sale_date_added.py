# Generated by Django 4.2.11 on 2024-04-06 13:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0003_sale_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2024, 4, 6, 13, 18, 52, 128998, tzinfo=datetime.timezone.utc)),
        ),
    ]
