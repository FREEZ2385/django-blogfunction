# Generated by Django 2.2.3 on 2019-08-08 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('blog_title', models.CharField(max_length=50)),
                ('blog_subtitle', models.CharField(max_length=100)),
                ('blog_contents', models.TextField()),
                ('blog_time', models.DateTimeField()),
                ('blog_num', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ['-blog_time'],
            },
        ),
    ]
