# Generated by Django 3.2.12 on 2022-03-31 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_admin', '0005_register_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer_hobby_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobbyid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_admin.hobby_name_tb')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_admin.register_tb')),
            ],
        ),
    ]
