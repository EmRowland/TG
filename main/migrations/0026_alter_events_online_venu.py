# Generated by Django 4.2.2 on 2023-08-19 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_alter_events_online_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='online_venu',
            field=models.URLField(help_text='Link to webinar', null=True, verbose_name='Webinar'),
        ),
    ]
