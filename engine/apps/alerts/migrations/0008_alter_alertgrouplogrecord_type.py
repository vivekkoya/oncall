# Generated by Django 3.2.16 on 2023-01-19 18:06

from django.db import migrations, models
import django_migration_linter as linter


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0007_populate_web_title_cache'),
    ]

    operations = [
        linter.IgnoreMigration(),
        migrations.AlterField(
            model_name='alertgrouplogrecord',
            name='type',
            field=models.IntegerField(choices=[(0, 'Acknowledged'), (1, 'Unacknowledged'), (2, 'Invite'), (3, 'Stop invitation'), (4, 'Re-invite'), (5, 'Escalation triggered'), (6, 'Invitation triggered'), (16, 'Escalation finished'), (7, 'Silenced'), (15, 'Unsilenced'), (8, 'Attached'), (9, 'Unattached'), (10, 'Custom button triggered'), (11, 'Unacknowledged by timeout'), (12, 'Failed attachment'), (13, 'Incident resolved'), (14, 'Incident unresolved'), (17, 'Escalation failed'), (18, 'Acknowledge reminder triggered'), (19, 'Wiped'), (20, 'Deleted'), (21, 'Incident registered'), (22, 'A route is assigned to the incident'), (23, 'Trigger direct paging escalation'), (24, 'Unpage a user')]),
        ),
    ]
