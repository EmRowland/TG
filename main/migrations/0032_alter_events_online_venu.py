# Generated by Django 4.2.2 on 2023-08-20 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_alter_events_online_status_alter_events_online_venu_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='online_venu',
            field=models.URLField(blank=True, help_text='Link To Webinar', null=True, verbose_name='Link To Webinar'),
        ),
    ]