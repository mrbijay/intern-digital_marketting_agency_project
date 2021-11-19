# Generated by Django 3.2.9 on 2021-11-17 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='Logo/')),
            ],
        ),
        migrations.CreateModel(
            name='Navbar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('href', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('order', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_title1', models.CharField(blank=True, max_length=100, null=True)),
                ('f_title2', models.CharField(blank=True, max_length=100, null=True)),
                ('f_title3', models.CharField(blank=True, max_length=100, null=True)),
                ('f_title4', models.CharField(blank=True, max_length=100, null=True)),
                ('f_title5', models.CharField(blank=True, max_length=100, null=True)),
                ('t1', models.CharField(blank=True, max_length=100, null=True)),
                ('t2', models.CharField(blank=True, max_length=100, null=True)),
                ('t3', models.CharField(blank=True, max_length=100, null=True)),
                ('t4', models.CharField(blank=True, max_length=100, null=True)),
                ('t5', models.CharField(blank=True, max_length=100, null=True)),
                ('a1', models.CharField(blank=True, max_length=100, null=True)),
                ('a2', models.CharField(blank=True, max_length=100, null=True)),
                ('a3', models.CharField(blank=True, max_length=100, null=True)),
                ('a4', models.CharField(blank=True, max_length=100, null=True)),
                ('a5', models.CharField(blank=True, max_length=100, null=True)),
                ('f_logo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.header')),
                ('nav_menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.navbar')),
            ],
        ),
    ]
