# Generated by Django 2.1.2 on 2018-11-07 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=150)),
                ('idade', models.IntegerField(blank=True, null=True)),
                ('celular', models.IntegerField(null=True)),
                ('email', models.CharField(blank=True, max_length=60)),
                ('cep', models.IntegerField(blank=True)),
                ('endereco', models.CharField(blank=True, max_length=150)),
                ('rg', models.IntegerField(blank=True)),
                ('cpf', models.IntegerField(blank=True)),
                ('descricao', models.TextField(blank=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='clientes_fotos')),
            ],
        ),
    ]