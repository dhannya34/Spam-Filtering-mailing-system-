# Generated by Django 3.2.12 on 2022-04-01 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_admin', '0009_auto_20220401_1039'),
    ]

    operations = [
        migrations.CreateModel(
            name='season_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seasonname', models.CharField(max_length=20)),
            ],
        ),
    ]