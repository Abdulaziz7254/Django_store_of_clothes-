# Generated by Django 5.0.4 on 2024-04-22 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Статья')),
                ('date', models.DateField()),
                ('author', models.CharField(max_length=50, verbose_name='Автор статьи')),
                ('image', models.ImageField(blank=True, null=True, upload_to='posters', verbose_name='Постер')),
                ('text', models.TextField(max_length=1000, verbose_name='Описание: ')),
            ],
        ),
    ]
