# Generated by Django 4.0.4 on 2022-05-09 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_telegramlog_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.IntegerField(null=True),
        ),
    ]
