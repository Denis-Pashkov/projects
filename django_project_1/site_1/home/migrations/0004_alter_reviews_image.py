# Generated by Django 3.2.9 on 2022-03-16 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_reviews_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='image',
            field=models.ImageField(default='', upload_to='images/', verbose_name='Изображение'),
        ),
    ]
