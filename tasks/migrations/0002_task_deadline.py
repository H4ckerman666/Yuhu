# Generated by Django 5.1.2 on 2024-10-29 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
