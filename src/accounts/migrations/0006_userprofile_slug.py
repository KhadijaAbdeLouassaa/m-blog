# Generated by Django 4.2.14 on 2024-08-26 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_userprofile_posts_saved_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]