# Generated by Django 4.0.4 on 2022-05-09 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_telegramlog_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegramlog',
            name='last_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
