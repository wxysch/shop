# Generated by Django 4.0.6 on 2022-07-20 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0010_aboutus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog_image/')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Блог',
                'verbose_name_plural': 'Блог',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('email', models.EmailField(max_length=100, verbose_name='Почта')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('phone', models.CharField(max_length=100, verbose_name='Телефонный номер')),
                ('problem', models.TextField(verbose_name='Проблема')),
                ('status', models.CharField(choices=[('В ожидании', 'В ожидании'), ('Решена', 'Решена'), ('Не решена', 'Не решена')], default='В ожидании', max_length=30, verbose_name='Статус обращения')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.AlterModelOptions(
            name='aboutus',
            options={'verbose_name': 'О нас', 'verbose_name_plural': 'О нас'},
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='title',
        ),
        migrations.AddField(
            model_name='aboutus',
            name='image',
            field=models.ImageField(default=1, upload_to='about_us/', verbose_name='Картинка о нас'),
            preserve_default=False,
        ),
    ]
