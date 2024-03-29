# Generated by Django 4.1 on 2023-08-03 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('art_gallery', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField()),
                ('gallery_img', models.ImageField(upload_to='media')),
                ('categoryid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='art_gallery.category')),
            ],
        ),
    ]
