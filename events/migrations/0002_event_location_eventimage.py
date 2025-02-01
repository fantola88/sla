# Generated by Django 5.1.5 on 2025-01-30 22:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(default='Local Desconhecido', max_length=255),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='EventImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='events.event')),
            ],
        ),
    ]
