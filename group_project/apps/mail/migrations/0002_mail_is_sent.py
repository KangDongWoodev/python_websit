# Generated by Django 5.0.6 on 2024-08-16 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mail',
            name='is_sent',
            field=models.BooleanField(default=False),
        ),
    ]
