# Generated by Django 4.2.7 on 2023-12-29 15:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0002_orderdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.product'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='total_sales',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='total_sales_amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=100),
        ),
    ]
