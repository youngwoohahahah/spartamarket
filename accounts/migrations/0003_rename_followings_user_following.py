# Generated by Django 4.2 on 2024-04-19 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_followings'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='followings',
            new_name='following',
        ),
    ]
