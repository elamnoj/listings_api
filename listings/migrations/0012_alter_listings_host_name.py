# Generated by Django 3.2.5 on 2021-07-16 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0011_alter_listings_host_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='host_name',
            field=models.CharField(max_length=500, null=True),
        ),
    ]