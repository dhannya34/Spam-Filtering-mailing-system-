# Generated by Django 3.2.12 on 2022-04-01 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_admin', '0011_seasonfactor_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='seasoncountry_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=20)),
                ('countryid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_admin.country_tb')),
                ('factorid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_admin.seasonfactor_tb')),
                ('seasonid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_admin.season_tb')),
                ('stateid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_admin.state_tb')),
            ],
        ),
    ]
