# Generated by Django 2.1 on 2019-01-26 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapi', '0004_auto_20190126_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='grouping',
            name='category',
            field=models.CharField(default='Academics', max_length=20),
        ),
        migrations.AddField(
            model_name='questionbank',
            name='board',
            field=models.CharField(default='CBSE', max_length=20),
        ),
        migrations.AddField(
            model_name='questionbank',
            name='category',
            field=models.CharField(default='Academics', max_length=20),
        ),
        migrations.AlterField(
            model_name='grouping',
            name='board',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='grouping',
            name='standard',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='grouping',
            name='subject',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='questionbank',
            name='standard',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='questionbank',
            name='subject',
            field=models.CharField(max_length=30),
        ),
    ]
