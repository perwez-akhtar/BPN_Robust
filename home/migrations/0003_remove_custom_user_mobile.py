# Generated by Django 5.0.3 on 2024-04-02 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='custom_user',
            name='mobile',
        ),
    ]
