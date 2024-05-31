# Generated by Django 5.0.1 on 2024-01-20 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_social_media_profile_github_profile_linkdin_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='github',
            new_name='college_location',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='location',
            new_name='home_location',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='twitter',
            new_name='instagram',
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
