# Generated by Django 4.1.7 on 2023-03-21 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produlct', models.CharField(max_length=5000, verbose_name='Товар')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=9999, verbose_name='Описание')),
                ('pice', models.IntegerField(verbose_name='Цена')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.prod', verbose_name='Наименование')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_price', models.IntegerField(verbose_name='Общая стоимость заказа')),
                ('prodct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.prod', verbose_name='Продукты')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producwt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.prod', verbose_name='Список товаров')),
            ],
        ),
    ]
