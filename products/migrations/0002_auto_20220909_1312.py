# Generated by Django 3.2 on 2022-09-09 11:12

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Rate')),
                ('review', models.TextField(max_length=500, verbose_name='Review')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created at')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.AddField(
            model_name='brand',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='brand_category', to='products.category'),
        ),
        migrations.AddField(
            model_name='product',
            name='desc',
            field=models.TextField(default='', max_length=1000, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='products/'),
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='product',
            name='flag',
            field=models.CharField(choices=[('New', 'New'), ('Feature', 'Feature'), ('Sale', 'Sale')], max_length=10, verbose_name='Flag'),
        ),
        migrations.AlterField(
            model_name='product',
            name='subtitle',
            field=models.CharField(max_length=500, verbose_name='Subtitle'),
        ),
        migrations.DeleteModel(
            name='ProductReviews',
        ),
        migrations.AddField(
            model_name='productreview',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_review', to='products.product', verbose_name='Product'),
        ),
        migrations.AddField(
            model_name='productreview',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_review', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
