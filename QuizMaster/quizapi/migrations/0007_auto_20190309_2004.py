# Generated by Django 2.1 on 2019-03-09 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizapi', '0006_auto_20190309_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userquiz',
            name='userId',
            field=models.ForeignKey(db_column='userId', on_delete=django.db.models.deletion.CASCADE, to='quizapi.UserDetails', to_field='userId'),
        ),
    ]
