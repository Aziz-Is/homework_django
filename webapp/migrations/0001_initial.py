# Generated by Django 4.0.5 on 2022-06-28 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Zagolovok')),
                ('text', models.TextField(max_length=3000, verbose_name='Text')),
                ('author', models.CharField(default='Unknown', max_length=40, verbose_name='Avtor')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Vremy sozdaniy')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Vremy izmeneniy')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
                'db_table': 'articles',
            },
        ),
    ]
