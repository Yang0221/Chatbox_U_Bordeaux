# Generated by Django 2.2.7 on 2020-04-10 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('localisation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='address',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='building',
            name='coordinates',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='building',
            name='id_campus',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='localisation.Campus'),
        ),
        migrations.AlterField(
            model_name='building',
            name='main_activity',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='campus',
            name='address',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='campus',
            name='coordinates',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='room',
            name='activity',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='room',
            name='floor',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='room',
            name='id_building',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='localisation.Building'),
        ),
    ]
