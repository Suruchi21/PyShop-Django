# Generated by Django 3.0.8 on 2021-02-11 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_offer'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='inCart',
            field=models.BooleanField(default=False),
        ),
    ]
