# Generated by Django 4.2 on 2024-04-19 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_followings_user_following'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_photo',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
