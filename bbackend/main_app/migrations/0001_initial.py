# Generated by Django 3.2.9 on 2021-11-04 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NavigationButtons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True, verbose_name='описание')),
                ('action_click_url', models.CharField(default='/', max_length=250, verbose_name='ссылка')),
                ('description', models.CharField(blank=True, max_length=250, null=True, verbose_name='описание')),
                ('value', models.IntegerField(blank=True, null=True, verbose_name='значение')),
            ],
            options={
                'verbose_name': 'навигация',
                'verbose_name_plural': 'навигацию',
            },
        ),
        migrations.CreateModel(
            name='NavigationDisplay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=250, null=True, verbose_name='описание')),
                ('value', models.IntegerField(blank=True, null=True, verbose_name='значение')),
                ('text', models.TextField(verbose_name='текст дисплея')),
                ('text_mode', models.CharField(default='HTML', max_length=15, verbose_name='мод текста')),
                ('is_endpoint_display', models.BooleanField(default=False, verbose_name='конечный диплей')),
                ('buttons', models.ManyToManyField(to='main_app.NavigationButtons', verbose_name='набор кнопок')),
            ],
            options={
                'verbose_name': 'навигация',
                'verbose_name_plural': 'навигацию',
            },
        ),
    ]
