# Generated by Django 3.1 on 2020-09-07 03:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employeeapi', '0002_auto_20200907_0510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='Team_leader_ID',
        ),
        migrations.CreateModel(
            name='Team_Leader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TeamName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employeeapi.team')),
                ('Team_Leader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employeeapi.employee')),
            ],
        ),
    ]
