# Generated by Django 4.2.2 on 2023-06-29 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('sub_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
