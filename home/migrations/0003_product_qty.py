# Generated by Django 4.1.1 on 2023-01-19 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_easypaisa_balance_easypaisa_in_easypaisa_balance_in_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='qty',
            field=models.IntegerField(default=1),
        ),
    ]
