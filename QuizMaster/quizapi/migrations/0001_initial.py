# Generated by Django 2.0.2 on 2018-07-07 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grouping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board', models.CharField(choices=[('CBSE', 'CBSE')], max_length=10)),
                ('standard', models.CharField(choices=[('1', 'First Std'), ('2', 'Second Std')], max_length=10)),
                ('subject', models.CharField(choices=[('E', 'Englist'), ('T', 'Tamil'), ('M', 'Maths')], max_length=10)),
                ('lessonNum', models.PositiveIntegerField(default=1)),
                ('lessonName', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionBank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard', models.CharField(choices=[('1', 'First Std'), ('2', 'Second Std')], max_length=10)),
                ('subject', models.CharField(choices=[('E', 'Englist'), ('T', 'Tamil'), ('M', 'Maths')], max_length=10)),
                ('difficulty', models.PositiveIntegerField(choices=[(1, 'Easy'), (2, 'Mid'), (3, 'Tough')])),
                ('marks', models.PositiveIntegerField(choices=[(1, 'One'), (2, 'Two'), (3, 'Three')])),
                ('lessonNum', models.PositiveIntegerField(default=1)),
                ('Q_image', models.URLField(blank=True, max_length=1000)),
                ('QuestionType', models.CharField(choices=[('1', 'Choose the best answer'), ('2', 'Choose multiple'), ('3', 'True or False'), ('4', 'Fill in the blanks'), ('5', 'Spelling Check')], default=1, max_length=1)),
                ('Question', models.CharField(max_length=1000)),
                ('answer_1', models.CharField(blank=True, max_length=200)),
                ('answer_1_ind', models.BooleanField(default=False)),
                ('answer_2', models.CharField(blank=True, max_length=200)),
                ('answer_2_ind', models.BooleanField(default=False)),
                ('answer_3', models.CharField(blank=True, max_length=200)),
                ('answer_3_ind', models.BooleanField(default=False)),
                ('answer_4', models.CharField(blank=True, max_length=200)),
                ('answer_4_ind', models.BooleanField(default=False)),
                ('answer_5', models.CharField(blank=True, max_length=200)),
                ('answer_5_ind', models.BooleanField(default=False)),
                ('answer_6', models.CharField(blank=True, max_length=200)),
                ('answer_6_ind', models.BooleanField(default=False)),
            ],
        ),
    ]
