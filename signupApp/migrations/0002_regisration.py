# Generated by Django 3.2 on 2021-06-29 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('signupApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='regisration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('pickupName', models.CharField(max_length=100)),
                ('parentLocation', models.CharField(max_length=100)),
                ('alergies', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signupApp.event')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signupApp.group')),
            ],
        ),
    ]
