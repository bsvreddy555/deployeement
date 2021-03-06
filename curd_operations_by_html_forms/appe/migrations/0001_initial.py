# Generated by Django 3.0.7 on 2020-07-04 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=100)),
                ('l_name', models.CharField(max_length=100)),
                ('mobile', models.BigIntegerField()),
                ('email', models.EmailField(max_length=50)),
                ('salary', models.FloatField()),
                ('experience', models.FloatField()),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('company', models.CharField(max_length=50)),
            ],
        ),
    ]
