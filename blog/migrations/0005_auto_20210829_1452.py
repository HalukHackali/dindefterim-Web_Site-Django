# Generated by Django 3.1.6 on 2021-08-29 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210829_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yazilarmodel',
            name='konular',
            field=models.ManyToManyField(related_name='yazi', to='blog.KonuModel'),
        ),
    ]
