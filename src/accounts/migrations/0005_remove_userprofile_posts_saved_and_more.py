# Generated by Django 4.2.14 on 2024-08-13 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_delete_postssaved'),
        ('accounts', '0004_userprofile_posts_saved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='posts_saved',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='posts_saved',
            field=models.ManyToManyField(blank=True, null=True, to='posts.post'),
        ),
    ]
