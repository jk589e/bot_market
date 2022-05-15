# Generated by Django 4.0.4 on 2022-05-15 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0005_alter_user_email_alter_user_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='photo1',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='items',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='discount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
    ]
