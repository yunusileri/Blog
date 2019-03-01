# Generated by Django 2.1.7 on 2019-03-01 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publishing_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Yayımlanma Tarihi'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(verbose_name='İçerik'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=128, verbose_name='Başlık'),
        ),
    ]