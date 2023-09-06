# Generated by Django 4.2.3 on 2023-09-06 20:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookmanagement', '0005_remove_review_reviewgivenby_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bookid', models.AutoField(primary_key=True, serialize=False)),
                ('bookname', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('isbn', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('stock', models.IntegerField()),
                ('isAvaiable', models.BooleanField(default=True)),
                ('publication_date', models.DateTimeField()),
                ('image', models.ImageField(blank=True, upload_to='bookcovers/')),
                ('page', models.IntegerField()),
                ('borrowedby', models.ManyToManyField(blank=True, related_name='borrowedbyRelated', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('categroyid', models.AutoField(primary_key=True, serialize=False)),
                ('categoryname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('reviewid', models.AutoField(primary_key=True, serialize=False)),
                ('reviewString', models.CharField(max_length=500)),
                ('reviewGivenBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('reviewOnBook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmanagement.book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='cat',
            field=models.ManyToManyField(blank=True, related_name='catRelated', to='bookmanagement.category'),
        ),
        migrations.AddField(
            model_name='book',
            name='wishlist',
            field=models.ManyToManyField(blank=True, related_name='wishlistRelated', to=settings.AUTH_USER_MODEL),
        ),
    ]