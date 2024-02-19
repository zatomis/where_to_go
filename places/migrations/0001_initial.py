# Generated by Django 5.0.2 on 2024-02-17 15:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Локация', max_length=100, unique=True, verbose_name='Название места')),
                ('short_description', models.TextField(blank=True, verbose_name='Описание места - кратко')),
                ('long_description', models.TextField(blank=True, verbose_name='Подробное описание места')),
                ('lon', models.FloatField(verbose_name='долгота')),
                ('lat', models.FloatField(verbose_name='широта')),
                ('slug', models.SlugField(blank=True, max_length=150, verbose_name='Уникальный идентификатор локации')),
                ('place_order', models.SmallIntegerField(db_index=True, default=0, verbose_name='Порядок сортировки')),
            ],
            options={
                'verbose_name': 'Место',
                'verbose_name_plural': 'Места',
                'ordering': ['place_order'],
            },
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='place_pic', verbose_name='Картинки')),
                ('pic_order', models.SmallIntegerField(db_index=True, default=0, verbose_name='Порядок сортировки')),
                ('place_pic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.place', verbose_name='Место')),
            ],
            options={
                'verbose_name': 'Картинка',
                'verbose_name_plural': 'Картинки',
                'ordering': ['pic_order'],
            },
        ),
    ]
