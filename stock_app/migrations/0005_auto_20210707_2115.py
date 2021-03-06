# Generated by Django 2.2 on 2021-07-08 04:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stock_app', '0004_stock_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='url',
            new_name='nasdaq_url',
        ),
        migrations.AddField(
            model_name='stock',
            name='news_url',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
