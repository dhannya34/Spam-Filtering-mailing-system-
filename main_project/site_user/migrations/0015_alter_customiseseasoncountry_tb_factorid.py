# Generated by Django 3.2.12 on 2022-04-11 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_admin', '0012_seasoncountry_tb'),
        ('site_user', '0014_alter_customiseseasoncountry_tb_factorid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customiseseasoncountry_tb',
            name='factorid',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='site_admin.seasonfactor_tb'),
        ),
    ]
