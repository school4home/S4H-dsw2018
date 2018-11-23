# Generated by Django 2.0.9 on 2018-11-23 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('year', models.ManyToManyField(related_name='modules', to='school.SchoolYear')),
            ],
        ),
    ]
