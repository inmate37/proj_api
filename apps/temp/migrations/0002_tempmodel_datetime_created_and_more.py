# Generated by Django 4.1.1 on 2022-09-14 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tempmodel',
            name='datetime_created',
            field=models.DateTimeField(auto_now_add=True, default='2022-01-01', verbose_name='время создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tempmodel',
            name='datetime_deleted',
            field=models.DateTimeField(blank=True, null=True, verbose_name='время удаления'),
        ),
        migrations.AddField(
            model_name='tempmodel',
            name='datetime_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='время обновления'),
        ),
    ]
