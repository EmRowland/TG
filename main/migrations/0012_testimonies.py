# Generated by Django 4.2.2 on 2023-07-08 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_events_event_status_to_come'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testimony', models.TextField()),
                ('username', models.CharField(max_length=200)),
                ('work', models.CharField(max_length=200)),
                ('image', models.ImageField(default='default.png', upload_to='testimonies')),
            ],
        ),
    ]
