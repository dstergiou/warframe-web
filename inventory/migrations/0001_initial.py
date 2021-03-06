# Generated by Django 4.0 on 2022-01-30 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url_name', models.CharField(max_length=100)),
                ('item_id', models.CharField(blank=True, default='__REPLACE__', max_length=100)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('ducats', models.PositiveIntegerField(blank=True, null=True)),
                ('rank', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
