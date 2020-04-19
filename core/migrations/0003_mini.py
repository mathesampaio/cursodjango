# Generated by Django 3.0.5 on 2020-04-19 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mini',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Mini Bacia')),
                ('vazao', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Vazão')),
                ('data', models.CharField(max_length=100, verbose_name='Data')),
            ],
        ),
    ]