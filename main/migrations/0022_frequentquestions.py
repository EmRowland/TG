# Generated by Django 4.2.2 on 2023-07-22 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_alter_events_options_alter_mahnazimages_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FrequentQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faq_question', models.CharField(max_length=1000)),
                ('faq_answer', models.CharField(max_length=1000)),
                ('faq_title', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Add faqs',
            },
        ),
    ]