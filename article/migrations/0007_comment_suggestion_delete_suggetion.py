# Generated by Django 5.0.4 on 2024-05-02 17:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_article_viewed'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=500, verbose_name='Comment')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.article')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suggestion', models.TextField(max_length=1000, verbose_name='suggetion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Suggetion',
        ),
    ]
