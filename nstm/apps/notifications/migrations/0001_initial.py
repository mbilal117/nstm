# Generated by Django 2.1 on 2018-08-12 20:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField(null=True)),
                ('action', models.PositiveSmallIntegerField(choices=[(1, 'Subscribers import completed'), (2, 'Subscribers import failed'), (3, 'Campaign sent')], verbose_name='action')),
                ('text', models.TextField(blank=True, verbose_name='text')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='date')),
                ('is_seen', models.BooleanField(default=False, verbose_name='seen status')),
                ('is_read', models.BooleanField(default=False, verbose_name='read status')),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contenttypes.ContentType', verbose_name='content type')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'notification',
                'verbose_name_plural': 'notifications',
                'db_table': 'nstm_notifications',
            },
        ),
    ]
