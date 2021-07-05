# Generated by Django 3.2.3 on 2021-07-05 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recompensa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recompensa', models.IntegerField(blank=True, null=True)),
                ('nombreUsuario', models.CharField(blank=True, max_length=99, null=True)),
                ('nombreEmpresaUsuario', models.CharField(blank=True, max_length=99, null=True)),
                ('producto', models.TextField(blank=True, max_length=99, null=True)),
                ('fechaCompra', models.DateTimeField()),
                ('statusRecompensa', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'ordering': ['fechaCompra'],
            },
        ),
    ]