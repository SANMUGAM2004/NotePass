# Generated by Django 5.0 on 2023-12-30 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
    ]
