# Generated by Django 4.2.2 on 2023-09-19 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_alter_mahnazcontacts_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='mahnazcontacts',
            name='country',
            field=models.CharField(blank=True, default='Canada', max_length=100, null=True, verbose_name='Add country'),
        ),
        migrations.AddField(
            model_name='mahnazcontacts',
            name='state',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Add state'),
        ),
        migrations.AddField(
            model_name='mahnazcontacts',
            name='street',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Add street'),
        ),
    ]