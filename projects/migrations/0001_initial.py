# Generated by Django 2.2.2 on 2019-06-14 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('logo_url', models.URLField(blank=True)),
                ('summary', models.TextField(blank=True, max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('url_name', models.CharField(default='Website', max_length=50)),
                ('url', models.URLField()),
                ('is_published', models.BooleanField(default=False)),
                ('date_published', models.DateField(blank=True)),
            ],
            options={
                'ordering': ['-is_published', '-date_published', '-date_created'],
            },
        ),
    ]
