# Generated by Django 4.0.3 on 2022-04-09 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0006_alter_advertisement_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advertisement',
            options={'ordering': ['created_at'], 'verbose_name': 'Объявление', 'verbose_name_plural': 'Объявления'},
        ),
    ]
