# Generated by Django 4.0.6 on 2022-07-17 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_galleryimage_show_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryimage',
            name='created_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Created at'),
        ),
    ]
