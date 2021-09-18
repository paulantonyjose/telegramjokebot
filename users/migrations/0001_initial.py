# Generated by Django 2.2 on 2021-09-18 03:10

from django.contrib.auth import get_user_model
from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserClickCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),

                ('type',models.CharField(verbose_name=('Joke Type'), max_length=100, blank=True, null=True)),
                ('joke', models.TextField(verbose_name=('Joke'), blank=True, null=True)),
                ('count', models.IntegerField(blank=True, null=True, verbose_name='Joke Click Count')),
            ],
            options={
                'db_table': 'userclickcount',
            },
        ),
    ]
