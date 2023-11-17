# Generated by Django 4.1 on 2023-11-16 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("biliscrapy", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="video", name="vname",),
        migrations.AddField(
            model_name="video",
            name="comment_fetched",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="video",
            name="danmu_fetched",
            field=models.BooleanField(default=False),
        ),
    ]
