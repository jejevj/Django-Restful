# Generated by Django 4.2.6 on 2023-10-16 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mahasiswa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nim', models.CharField(max_length=10)),
                ('nama', models.CharField(max_length=100)),
                ('kelas', models.CharField(max_length=1)),
                ('created_at', models.DateField(auto_now=True)),
            ],
        ),
    ]