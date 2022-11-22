# Generated by Django 4.1.3 on 2022-11-21 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Blog", "0002_readinglist_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="comment",
            field=models.TextField(max_length=255, verbose_name="Comment"),
        ),
        migrations.AlterField(
            model_name="post",
            name="post_url",
            field=models.CharField(max_length=255, unique=True, verbose_name="URL"),
        ),
        migrations.AlterField(
            model_name="post",
            name="short_description",
            field=models.TextField(max_length=255, verbose_name="Short Description"),
        ),
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(max_length=255, verbose_name="Add Title"),
        ),
    ]
