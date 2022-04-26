# Generated by Django 3.2.12 on 2022-03-30 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_admin', '0003_country_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='state_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=20)),
                ('countryid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_admin.country_tb')),
            ],
        ),
    ]
