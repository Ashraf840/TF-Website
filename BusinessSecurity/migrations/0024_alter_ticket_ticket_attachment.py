# Generated by Django 3.2.7 on 2022-01-17 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BusinessSecurity', '0023_alter_business_zipcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ticket_attachment',
            field=models.FileField(upload_to='ticket/', verbose_name='Attachment'),
        ),
    ]
