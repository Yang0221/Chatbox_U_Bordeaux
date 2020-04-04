# Generated by Django 2.2.7 on 2020-04-04 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('main_activity', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=500)),
                ('coordinates', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=500)),
                ('coordinates', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('floor', models.IntegerField()),
                ('activity', models.CharField(max_length=255)),
                ('id_building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='localisation.Building')),
            ],
        ),
        migrations.CreateModel(
            name='SynonymRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255)),
                ('id_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='localisation.Room')),
            ],
        ),
        migrations.CreateModel(
            name='SynonymCampus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255)),
                ('id_campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='localisation.Campus')),
            ],
        ),
        migrations.CreateModel(
            name='SynonymBuilding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255)),
                ('id_building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='localisation.Building')),
            ],
        ),
        migrations.AddField(
            model_name='building',
            name='id_campus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='localisation.Campus'),
        ),
    ]
