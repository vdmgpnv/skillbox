# Generated by Django 4.0.3 on 2022-04-09 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0004_alter_advertisement_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='title',
            field=models.CharField(db_index=True, max_length=1000, verbose_name='Заголовок'),
        ),
    ]