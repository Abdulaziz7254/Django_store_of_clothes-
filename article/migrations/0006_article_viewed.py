# Generated by Django 5.0.4 on 2024-05-01 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_suggetion'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='viewed',
            field=models.IntegerField(default=0),
        ),
    ]
