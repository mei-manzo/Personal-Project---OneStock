# Generated by Django 2.2 on 2021-07-09 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock_app', '0007_auto_20210708_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='stock',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='stock_app.Stock'),
        ),
        migrations.AlterField(
            model_name='article',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_articles', to='stock_app.User'),
        ),
    ]
