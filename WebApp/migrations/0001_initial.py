# Generated by Django 3.0.5 on 2020-06-14 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StdModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StdNo', models.IntegerField()),
                ('StdName', models.CharField(max_length=300)),
                ('StdPic', models.FileField(blank=True, null=True, upload_to='')),
                ('stdAds', models.CharField(max_length=300)),
            ],
        ),
    ]
