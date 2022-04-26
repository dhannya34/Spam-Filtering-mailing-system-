# Generated by Django 3.2.12 on 2022-03-30 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_admin', '0004_state_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='register_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('dob', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('securityquestion', models.CharField(max_length=20)),
                ('answer', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_admin.country_tb')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_admin.state_tb')),
            ],
        ),
    ]