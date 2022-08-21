# Generated by Django 4.1 on 2022-08-21 21:18

import ChatApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChatApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='chat_avatar',
            field=models.ImageField(default=1, upload_to=ChatApp.models.chat_avatar_path),
            preserve_default=False,
        ),
    ]
