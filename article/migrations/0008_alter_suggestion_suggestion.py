# Generated by Django 5.0.4 on 2024-05-03 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_comment_suggestion_delete_suggetion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suggestion',
            name='suggestion',
            field=models.TextField(max_length=1000, verbose_name='suggestion'),
        ),
    ]