# Generated by Django 5.0.3 on 2024-03-25 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_delete_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='name',
            new_name='doctor_name',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='name',
            new_name='patient_name',
        ),
    ]
