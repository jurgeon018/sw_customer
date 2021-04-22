# Generated by Django 3.2 on 2021-04-22 14:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sw_currency', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Назва купона')),
                ('discount_amount', models.FloatField(verbose_name='Знижка')),
                ('discount_type', models.CharField(choices=[('currency', 'сумма'), ('percent', '%')], default=0, max_length=255, verbose_name='Тип знижки')),
                ('requisition', models.FloatField(default=0, help_text='Мінімальна сума, на яку потрібно зробити замовлення, щоб купон набув дійсності.', verbose_name='Умова')),
                ('started', models.DateTimeField(verbose_name='Дата початку')),
                ('period', models.DateTimeField(blank=True, null=True, verbose_name='Термін дії')),
                ('currency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sw_currency.currency', verbose_name='Валюта')),
                ('users', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Користувачі')),
            ],
            options={
                'verbose_name': 'купон',
                'verbose_name_plural': 'Список купонів',
            },
        ),
    ]
