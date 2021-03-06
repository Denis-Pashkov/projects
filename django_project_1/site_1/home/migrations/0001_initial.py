# Generated by Django 3.2.9 on 2022-02-26 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15, verbose_name='Имя пользователя')),
                ('title', models.CharField(max_length=30, verbose_name='Тема(Заголовок)')),
                ('rewiew', models.TextField(verbose_name='Отзыв')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]
