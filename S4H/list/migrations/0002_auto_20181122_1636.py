# Generated by Django 2.0.9 on 2018-11-22 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20181122_1557'),
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=0, max_digits=1)),
            ],
        ),
        migrations.CreateModel(
            name='GradeObserver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='grade',
            name='grade_observer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='list.GradeObserver'),
        ),
        migrations.AddField(
            model_name='grade',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.S4HUser'),
        ),
    ]