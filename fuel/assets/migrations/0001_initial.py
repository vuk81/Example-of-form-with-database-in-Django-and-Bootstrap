# Generated by Django 2.0 on 2017-12-16 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chemicals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iupac_name', models.CharField(max_length=100)),
                ('manufacuturer', models.CharField(max_length=100)),
                ('data_enter', models.DateField(auto_now=True)),
                ('data_expire', models.DateField()),
                ('chem_status', models.BooleanField(default=True)),
            ],
        ),
    ]
