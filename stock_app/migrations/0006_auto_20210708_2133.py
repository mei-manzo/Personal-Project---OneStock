# Generated by Django 2.2 on 2021-07-09 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_app', '0005_auto_20210707_2115'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hyperlink', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='stock',
            name='article_users',
            field=models.ManyToManyField(related_name='article_users', to='stock_app.User'),
        ),
    ]
