# Generated by Django 3.1.5 on 2021-01-29 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PacketFlow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_src', models.TextField()),
                ('ip_dst', models.TextField()),
            ],
        ),
    ]
