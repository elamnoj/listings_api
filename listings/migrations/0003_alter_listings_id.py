# Generated by Django 3.2.5 on 2021-07-15 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_alter_listings_reviews_per_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
