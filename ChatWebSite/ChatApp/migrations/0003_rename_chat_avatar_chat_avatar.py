# Generated by Django 4.1 on 2022-08-21 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChatApp', '0002_chat_chat_avatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='chat_avatar',
            new_name='avatar',
        ),
    ]