# Generated by Django 4.1 on 2023-08-03 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art_gallery', '0003_gallerymodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallerymodel',
            name='gallery_img',
            field=models.ImageField(upload_to='media/% Y'),
        ),
    ]
