# Generated by Django 3.0.7 on 2023-06-13 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('admin', 'Admin'), ('client', 'Client'), ('owner_arena', 'Owner Arena')], max_length=15, null=True),
        ),
    ]
