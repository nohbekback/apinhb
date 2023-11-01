# Generated by Django 4.2.6 on 2023-11-01 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('createdat', models.DateTimeField(auto_now_add=True)),
                ('updatedat', models.DateTimeField(auto_now=True)),
                ('lastrecord', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idstatus', models.IntegerField()),
                ('idrol', models.IntegerField()),
                ('createdat', models.DateTimeField(auto_now_add=True)),
                ('updatedat', models.DateTimeField(auto_now=True)),
                ('lastrecord', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_app.tuser')),
            ],
        ),
        migrations.CreateModel(
            name='TLOGIN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idstatus', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('createdat', models.DateTimeField(auto_now_add=True)),
                ('updatedat', models.DateTimeField(auto_now=True)),
                ('lastrecord', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_app.tuser')),
            ],
        ),
    ]