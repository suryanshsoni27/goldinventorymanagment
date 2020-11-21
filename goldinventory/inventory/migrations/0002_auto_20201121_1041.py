# Generated by Django 3.0.7 on 2020-11-21 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diamonds',
            name='status',
            field=models.CharField(choices=[('AVAILABLE', 'Item ready to be sold'), ('SOLD', 'Item sold'), ('In production', 'Item in manufacturing')], default='not available', max_length=100),
        ),
        migrations.AlterField(
            model_name='earring',
            name='status',
            field=models.CharField(choices=[('AVAILABLE', 'Item ready to be sold'), ('SOLD', 'Item sold'), ('In production', 'Item in manufacturing')], default='not available', max_length=100),
        ),
        migrations.AlterField(
            model_name='rings',
            name='status',
            field=models.CharField(choices=[('AVAILABLE', 'Item ready to be sold'), ('SOLD', 'Item sold'), ('In production', 'Item in manufacturing')], default='not available', max_length=100),
        ),
    ]