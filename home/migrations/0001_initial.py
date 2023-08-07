# Generated by Django 3.2.18 on 2023-04-15 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(max_length=10)),
                ('year', models.IntegerField(max_length=3)),
                ('pt', models.CharField(max_length=3)),
                ('question1', models.IntegerField(max_length=4)),
                ('question2', models.IntegerField(max_length=4)),
                ('question3', models.IntegerField(max_length=4)),
                ('question4', models.IntegerField(max_length=4)),
                ('question5', models.IntegerField(max_length=4)),
                ('question6', models.IntegerField(max_length=4)),
                ('question7', models.IntegerField(max_length=4)),
                ('question8', models.IntegerField(max_length=4)),
            ],
            options={
                'db_table': 'course_tabel_name',
            },
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('roll_no', models.IntegerField(max_length=10, primary_key=True, serialize=False)),
                ('branch', models.CharField(max_length=10)),
                ('year', models.IntegerField(max_length=3)),
                ('pt', models.CharField(max_length=3)),
                ('question1', models.IntegerField(max_length=4)),
                ('question2', models.IntegerField(max_length=4)),
                ('question3', models.IntegerField(max_length=4)),
                ('question4', models.IntegerField(max_length=4)),
                ('question5', models.IntegerField(max_length=4)),
                ('question6', models.IntegerField(max_length=4)),
                ('question7', models.IntegerField(max_length=4)),
                ('question8', models.IntegerField(max_length=4)),
            ],
            options={
                'db_table': 'marks_tabel_name',
            },
        ),
    ]