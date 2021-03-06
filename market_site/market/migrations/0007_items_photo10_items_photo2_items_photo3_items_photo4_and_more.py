

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0006_items_photo1_alter_items_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='photo10',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='items',
            name='photo2',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='items',
            name='photo3',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='items',
            name='photo4',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='items',
            name='photo5',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='items',
            name='photo6',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='items',
            name='photo7',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='items',
            name='photo8',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='items',
            name='photo9',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),

        migrations.AddField(
            model_name='user',
            name='user_photo',
            field=models.ImageField(blank=True, null=True, upload_to='userphotos/'),
        ),
        ]

