# Generated by Django 3.2.12 on 2022-04-04 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_admin', '0012_seasoncountry_tb'),
        ('site_user', '0004_contact_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='blacklist_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('date', models.CharField(max_length=20)),
                ('time', models.CharField(max_length=20)),
                ('remarks', models.CharField(max_length=20)),
                ('contactidd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contactidd', to='site_admin.register_tb')),
                ('useridd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='useridd', to='site_admin.register_tb')),
            ],
        ),
    ]
