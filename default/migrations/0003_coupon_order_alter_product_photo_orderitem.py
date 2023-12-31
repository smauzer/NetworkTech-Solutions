# Generated by Django 4.2.6 on 2023-11-02 09:24

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0002_alter_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('uses', models.IntegerField(default=0)),
                ('expiration_date', models.DateTimeField(blank=True)),
                ('products_precentage_off', models.DecimalField(decimal_places=0, default=0, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('shipping_precentage_off', models.DecimalField(decimal_places=0, default=0, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('postal', models.IntegerField()),
                ('city', models.CharField(max_length=35)),
                ('address', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('order_price', models.IntegerField()),
                ('shipping_price', models.IntegerField()),
                ('total_price', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(upload_to='termekek'),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('final_price_per_unit', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='default.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='default.product')),
            ],
        ),
    ]
