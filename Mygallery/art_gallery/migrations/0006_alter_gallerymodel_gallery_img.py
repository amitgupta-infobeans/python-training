# Generated by Django 4.1 on 2023-08-03 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art_gallery', '0005_alter_gallerymodel_gallery_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallerymodel',
            name='gallery_img',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]
