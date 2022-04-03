# Generated by Django 3.1.7 on 2022-04-03 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=45)),
                ('ticket', models.CharField(max_length=450)),
                ('tempomonitoramento', models.IntegerField()),
                ('iniciomonitoramentoemdias', models.IntegerField()),
                ('terminomonitoramentoemdias', models.IntegerField()),
                ('email', models.CharField(max_length=100)),
                ('valormenor', models.DecimalField(decimal_places=2, max_digits=9)),
                ('valormaior', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
        ),
    ]
