# Generated by Django 5.0.4 on 2024-05-14 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('discription', models.TextField()),
                ('cite_URl', models.URLField()),
                ('star', models.DecimalField(decimal_places=1, max_digits=2)),
                ('like', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cinema', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=15)),
            ],
        ),
    ]
