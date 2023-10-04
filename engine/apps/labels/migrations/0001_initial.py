# Generated by Django 3.2.20 on 2023-09-26 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('alerts', '0032_remove_alertgroup_slack_message_state'),
        ('user_management', '0014_auto_20230728_0802'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabelKeyCache',
            fields=[
                ('id', models.CharField(editable=False, max_length=36, primary_key=True, serialize=False)),
                ('repr', models.CharField(max_length=200)),
                ('last_synced', models.DateTimeField(auto_now=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_management.organization')),
            ],
        ),
        migrations.CreateModel(
            name='LabelValueCache',
            fields=[
                ('id', models.CharField(editable=False, max_length=36, primary_key=True, serialize=False)),
                ('repr', models.CharField(max_length=200)),
                ('last_synced', models.DateTimeField(auto_now=True)),
                ('key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='values', to='labels.labelkeycache')),
            ],
        ),
        migrations.CreateModel(
            name='AlertReceiveChannelAssociatedLabel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alert_receive_channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='labels', to='alerts.alertreceivechannel')),
                ('key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labels.labelkeycache')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='labels', to='user_management.organization')),
                ('value', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labels.labelvaluecache')),
            ],
            options={
                'unique_together': {('key_id', 'value_id', 'alert_receive_channel_id')},
            },
        ),
    ]