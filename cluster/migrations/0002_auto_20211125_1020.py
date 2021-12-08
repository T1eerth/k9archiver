# Generated by Django 3.2.8 on 2021-11-25 10:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cluster', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clustermodel',
            name='permission',
            field=models.CharField(choices=[('PO', 'Participant Only'), ('p', 'Public')], default='PO', max_length=10),
        ),
        migrations.AddField(
            model_name='notemodel',
            name='body',
            field=models.CharField(default='Empty', max_length=1200),
        ),
        migrations.AlterField(
            model_name='clustermodel',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CluseterModel_User', to=settings.AUTH_USER_MODEL),
        ),
    ]
