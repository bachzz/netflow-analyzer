# Generated by Django 3.1.5 on 2021-02-11 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20210211_0355'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgentStatus',
            fields=[
                ('agent_id', models.TextField(primary_key=True, serialize=False)),
                ('status', models.IntegerField(default=0)),
            ],
        ),
    ]
