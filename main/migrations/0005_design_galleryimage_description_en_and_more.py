# Generated by Django 4.0.6 on 2022-07-21 19:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_galleryimage_high_galleryimage_wide'),
    ]

    operations = [
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True)),
                ('title_ru', models.TextField(blank=True, null=True)),
                ('title_en', models.TextField(blank=True, null=True)),
                ('title_he', models.TextField(blank=True, null=True)),
                ('subtitle', models.TextField(blank=True)),
                ('subtitle_ru', models.TextField(blank=True, null=True)),
                ('subtitle_en', models.TextField(blank=True, null=True)),
                ('subtitle_he', models.TextField(blank=True, null=True)),
                ('background', models.ImageField(upload_to='photos/BACKGROUND/%y/%m/%d')),
                ('about_picture', models.ImageField(upload_to='photos/ABOUT-PICS/%y/%m/%d')),
                ('about_title', models.CharField(max_length=50)),
                ('about_title_ru', models.CharField(max_length=50, null=True)),
                ('about_title_en', models.CharField(max_length=50, null=True)),
                ('about_title_he', models.CharField(max_length=50, null=True)),
                ('about_subtitle', models.CharField(max_length=50)),
                ('about_subtitle_ru', models.CharField(max_length=50, null=True)),
                ('about_subtitle_en', models.CharField(max_length=50, null=True)),
                ('about_subtitle_he', models.CharField(max_length=50, null=True)),
                ('about_text', models.TextField(blank=True)),
                ('about_text_ru', models.TextField(blank=True, null=True)),
                ('about_text_en', models.TextField(blank=True, null=True)),
                ('about_text_he', models.TextField(blank=True, null=True)),
                ('footer_text', models.TextField(blank=True)),
                ('footer_text_ru', models.TextField(blank=True, null=True)),
                ('footer_text_en', models.TextField(blank=True, null=True)),
                ('footer_text_he', models.TextField(blank=True, null=True)),
                ('display', models.BooleanField(db_index=True, verbose_name='Display this design?')),
            ],
            options={
                'verbose_name': 'Site design',
                'verbose_name_plural': 'Site designs',
                'ordering': ('display',),
            },
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='description_en',
            field=models.TextField(blank=True, null=True, validators=[django.core.validators.MaxLengthValidator(350, message='The text is too long, it should be a maximum of 350 characters.')], verbose_name='Short image description'),
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='description_he',
            field=models.TextField(blank=True, null=True, validators=[django.core.validators.MaxLengthValidator(350, message='The text is too long, it should be a maximum of 350 characters.')], verbose_name='Short image description'),
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='description_ru',
            field=models.TextField(blank=True, null=True, validators=[django.core.validators.MaxLengthValidator(350, message='The text is too long, it should be a maximum of 350 characters.')], verbose_name='Short image description'),
        ),
        migrations.AlterField(
            model_name='galleryimage',
            name='Image',
            field=models.ImageField(upload_to='photos/GALLERY/%y/%m/%d', verbose_name='Image in gallery'),
        ),
    ]
