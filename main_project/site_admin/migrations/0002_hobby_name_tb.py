# Generated by Django 3.2.12 on 2022-03-30 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='hobby_name_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobbyname', models.CharField(max_length=20)),
            ],
        ),
    ]