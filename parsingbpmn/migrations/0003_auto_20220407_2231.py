# Generated by Django 3.1.2 on 2022-04-07 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parsingbpmn', '0002_auto_20220406_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='process',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parsingbpmn.process'),
        ),
    ]