# Generated by Django 4.0.4 on 2022-05-03 21:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('image', models.CharField(max_length=250)),
                ('movielink', models.CharField(default='', max_length=250)),
                ('movieposter', models.CharField(max_length=250)),
                ('genre', models.CharField(choices=[('Romantic Comedy', 'Romantic Comedy'), ('Thrillers', 'Thrillers'), ('Drama', 'Drama'), ('Comedy', 'Comedy'), ('Documentary', 'Documentary'), ('Family', 'Family')], default='Romantic Comedy', max_length=15)),
                ('favorites', models.ManyToManyField(blank=True, default=None, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=100)),
                ('recommend', models.BooleanField(verbose_name='Would Recommend')),
                ('movie', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='main_app.movie')),
                ('user', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=600)),
                ('image', models.CharField(max_length=250)),
                ('genre', models.CharField(choices=[('Romantic Comedy', 'Romantic Comedy'), ('Thrillers', 'Thrillers'), ('Drama', 'Drama'), ('Comedy', 'Comedy'), ('Documentary', 'Documentary'), ('Family', 'Family')], default='Romantic Comedy', max_length=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
