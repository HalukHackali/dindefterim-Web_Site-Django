# Generated by Django 3.1.6 on 2021-08-29 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20210829_1725'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='choice',
            options={'verbose_name': 'Seçenek', 'verbose_name_plural': 'Seçenekler'},
        ),
        migrations.AlterModelTable(
            name='choice',
            table='Seçenek',
        ),
    ]
