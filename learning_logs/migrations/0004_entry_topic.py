# Generated by Django 4.1.2 on 2022-10-16 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0003_remove_entry_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='topic',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='learning_logs.topic'),
            preserve_default=False,
        ),
    ]
