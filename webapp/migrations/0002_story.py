# Generated by Django 4.0.5 on 2022-06-28 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_chapter', models.CharField(max_length=100, verbose_name='asus')),
                ('second_chapter', models.TextField(max_length=1000, verbose_name='acer')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Vremy sozdaniy')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Vremy izmeneniy')),
            ],
            options={
                'verbose_name': 'istoriy',
                'verbose_name_plural': 'istorii',
                'db_table': 'stories',
            },
        ),
    ]