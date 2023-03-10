# Generated by Django 3.2 on 2022-09-09 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='company')),
                ('call_us', models.CharField(max_length=100)),
                ('email_us', models.EmailField(max_length=254)),
                ('subtitle', models.TextField(max_length=500)),
                ('fb_link', models.URLField(blank=True, null=True)),
                ('twit_link', models.URLField(blank=True, null=True)),
                ('insta_link', models.URLField(blank=True, null=True)),
                ('emails', models.TextField(max_length=100)),
                ('numbers', models.TextField(max_length=100)),
                ('address', models.TextField(max_length=100)),
            ],
        ),
    ]
