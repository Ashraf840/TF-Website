# Generated by Django 3.2.7 on 2022-01-18 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BusinessSecurity', '0026_notification_is_new'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='is_new',
            new_name='is_read',
        ),
    ]
