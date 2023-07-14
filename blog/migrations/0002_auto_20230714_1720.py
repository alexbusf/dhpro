# Generated by Django 3.2 on 2023-07-14 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.CharField(default='test', max_length=160, verbose_name='Description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='test'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
