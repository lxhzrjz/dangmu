# Generated by Django 4.1 on 2023-11-17 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("biliscrapy", "0003_rename_bvid_bilidanmu_cid"),
    ]

    operations = [
        migrations.RenameModel(old_name="Video", new_name="BiliVideo",),
    ]
