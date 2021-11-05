# Generated by Django 3.2.9 on 2021-11-05 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20211105_2107'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='navigationdisplay',
            options={'verbose_name': 'Дисплей', 'verbose_name_plural': 'Дисплеи'},
        ),
        migrations.RemoveField(
            model_name='navigationdisplay',
            name='is_endpoint_display',
        ),
        migrations.AddField(
            model_name='navigationdisplay',
            name='content',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ссылка на контент'),
        ),
    ]
