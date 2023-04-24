# Generated by Django 4.2 on 2023-04-11 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appli', '0004_delete_settings_remove_product_product_gender_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.DeleteModel(
            name='Price',
        ),
        migrations.AddField(
            model_name='product',
            name='product_gender',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='appli.gender'),
        ),
    ]