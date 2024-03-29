# Generated by Django 4.0.4 on 2022-05-24 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categoria', '0001_initial'),
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('preco', models.FloatField(max_length=10)),
                ('categoria', models.ManyToManyField(to='categoria.categoria')),
                ('cliente_proprietario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cliente.cliente')),
            ],
        ),
    ]
