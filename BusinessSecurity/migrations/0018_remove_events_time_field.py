# Generated by Django 3.2.7 on 2022-01-07 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BusinessSecurity', '0017_alter_events_timezone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='time_field',
        ),
    ]
