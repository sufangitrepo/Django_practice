# Generated by Django 4.1 on 2022-08-14 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorModel',
            fields=[
                ('id', models.IntegerField(max_length=10000, primary_key=True, serialize=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=True, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('tagline', models.CharField(max_length=300)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogers.authormodel')),
            ],
        ),
        migrations.CreateModel(
            name='EntryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=True, verbose_name='ID')),
                ('detail', models.TextField()),
                ('rating', models.CharField(max_length=20)),
                ('published_date', models.DateField()),
                ('blog_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogers.blogmodel')),
            ],
        ),
    ]
