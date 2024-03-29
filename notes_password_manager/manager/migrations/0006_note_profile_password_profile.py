# Generated by Django 5.0 on 2023-12-30 12:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='profile',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.profile'),
        ),
        migrations.AddField(
            model_name='password',
            name='profile',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.profile'),
        ),
    ]
