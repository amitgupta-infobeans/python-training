# Generated by Django 4.1 on 2023-08-01 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0002_rename_urlfield_userprofileinfo_portfolio_site_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(max_length=160)),
                ('last_name', models.TextField(max_length=160)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('desc', models.TextField(blank=True)),
            ],
        ),
    ]
