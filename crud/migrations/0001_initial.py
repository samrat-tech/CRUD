# Generated by Django 4.0.4 on 2022-04-25 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.IntegerField()),
                ('name', models.CharField(default='none', max_length=64, null=True)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
