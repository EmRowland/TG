# Generated by Django 4.2.2 on 2023-07-22 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_alter_events_options_alter_ourimages_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='events',
            options={'verbose_name': 'Add Event'},
        ),
        migrations.AlterModelOptions(
            name='mahnazimages',
            options={'verbose_name': 'Add Images Of Mahnaz'},
        ),
        migrations.AlterModelOptions(
            name='ourimages',
            options={'verbose_name': 'Add Art Image'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at'], 'verbose_name': 'Add Blog Post'},
        ),
        migrations.AlterModelOptions(
            name='subscribers',
            options={'verbose_name': 'See Subscribed User'},
        ),
        migrations.AlterModelOptions(
            name='subscribetoevent',
            options={'verbose_name': ' See Event Subscription'},
        ),
        migrations.AlterModelOptions(
            name='testimonies',
            options={'verbose_name': 'Add Testimonie'},
        ),
    ]