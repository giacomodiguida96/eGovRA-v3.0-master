# Generated by Django 4.0.3 on 2022-03-14 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parsingbpmn', '0002_remove_risk_threat_risk_impact_risk_likelihood_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataObject_id',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_dataobj', models.CharField(max_length=100)),
                ('id_dataobj_ref', models.CharField(max_length=100)),
                ('asset', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='parsingbpmn.asset')),
            ],
        ),
    ]