# Generated by Django 4.2.2 on 2023-07-06 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_rename_event_status_events_event_status_to_come'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='event_status_to_come',
            field=models.BooleanField(default=True),
        ),
    ]
