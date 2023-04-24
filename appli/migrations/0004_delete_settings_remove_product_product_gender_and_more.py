# Generated by Django 4.2 on 2023-04-11 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appli', '0003_category_price_settings_size'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Settings',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_gender',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_promoted',
        ),
        migrations.AddField(
            model_name='product',
            name='product_description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_promotion_start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_sizes',
            field=models.ManyToManyField(to='appli.size'),
        ),
        migrations.AlterField(
            model_name='price',
            name='title',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appli.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appli.price'),
        ),
        migrations.AlterField(
            model_name='size',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]