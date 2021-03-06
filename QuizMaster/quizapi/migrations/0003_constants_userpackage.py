# Generated by Django 2.1 on 2018-12-28 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapi', '0002_auto_20181215_1532'),
    ]

    operations = [
        migrations.CreateModel(
            name='Constants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('varName', models.CharField(blank=True, max_length=40)),
                ('varSeqNo', models.PositiveIntegerField(default=0)),
                ('varValue', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='UserPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=50)),
                ('paymentGateway', models.CharField(max_length=20)),
                ('packageId', models.CharField(blank=True, max_length=20)),
                ('paymentId', models.CharField(blank=True, max_length=200)),
                ('paymentId2', models.CharField(blank=True, max_length=200)),
                ('requestId', models.CharField(blank=True, max_length=200)),
                ('paymentDate', models.CharField(blank=True, max_length=50)),
                ('startDate', models.CharField(blank=True, max_length=50)),
                ('endDate', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
