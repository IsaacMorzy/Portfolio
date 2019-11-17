# Generated by Django 2.2.2 on 2019-06-14 19:19

from django.db import migrations, models
import markdownx.models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('cover_image_url', models.URLField(blank=True)),
                ('cover_image_credit_badge', models.TextField(blank=True)),
                ('summary', models.TextField(blank=True, max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('text', markdownx.models.MarkdownxField()),
                ('is_published', models.BooleanField(default=False)),
                ('date_published', models.DateTimeField(blank=True)),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ['-is_published', '-date_published', '-date_created'],
            },
        ),
    ]
