# Generated by Django 2.0.9 on 2018-11-22 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('close_date', models.DateField()),
                ('description', models.CharField(max_length=500)),
                ('Question', models.TextField(blank=True, null=True)),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_list.exercise_set+', to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ImageQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('close_date', models.DateField()),
                ('description', models.CharField(max_length=500)),
                ('photo', models.ImageField(upload_to='photoQuestion')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_list.imagequestion_set+', to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TextQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('close_date', models.DateField()),
                ('description', models.CharField(max_length=500)),
                ('text', models.TextField(blank=True, null=True)),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_list.textquestion_set+', to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VideoQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('close_date', models.DateField()),
                ('description', models.CharField(max_length=500)),
                ('video', models.TextField(blank=True, null=True)),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_list.videoquestion_set+', to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
