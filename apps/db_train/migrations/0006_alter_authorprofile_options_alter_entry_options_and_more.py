# Generated by Django 4.2.5 on 2024-10-21 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db_train', '0005_tag_entry_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='authorprofile',
            options={'verbose_name': 'Профиль автора', 'verbose_name_plural': 'Профили авторов'},
        ),
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name': 'Статья', 'verbose_name_plural': 'Наши статьи'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Тег', 'verbose_name_plural': 'Теги'},
        ),
    ]
