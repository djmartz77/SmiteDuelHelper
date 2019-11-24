# Generated by Django 2.2.4 on 2019-11-24 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='p1_active_1',
        ),
        migrations.RemoveField(
            model_name='match',
            name='p1_active_2',
        ),
        migrations.RemoveField(
            model_name='match',
            name='p1_duel_tier',
        ),
        migrations.RemoveField(
            model_name='match',
            name='p1_god',
        ),
        migrations.RemoveField(
            model_name='match',
            name='p1_item_1',
        ),
        migrations.RemoveField(
            model_name='match',
            name='p1_item_2',
        ),
        migrations.RemoveField(
            model_name='match',
            name='p1_item_3',
        ),
        migrations.RemoveField(
            model_name='match',
            name='p1_item_4',
        ),
        migrations.RemoveField(
            model_name='match',
            name='p1_item_5',
        ),
        migrations.RemoveField(
            model_name='match',
            name='p1_item_6',
        ),
        migrations.RemoveField(
            model_name='match',
            name='p1_name',
        ),
        migrations.RemoveField(
            model_name='match',
            name='p1_win_status',
        ),
        migrations.RemoveField(
            model_name='match',
            name='p2_active_1',
        ),
        migrations.RemoveField(
            model_name='match',
            name='p2_active_2',
        ),
        migrations.RemoveField(
            model_name='match',
            name='p2_duel_tier',
        ),
        migrations.RemoveField(
            model_name='match',
            name='p2_god',
        ),
        migrations.RemoveField(
            model_name='match',
            name='p2_item_1',
        ),
        migrations.RemoveField(
            model_name='match',
            name='p2_item_2',
        ),
        migrations.RemoveField(
            model_name='match',
            name='p2_item_3',
        ),
        migrations.RemoveField(
            model_name='match',
            name='p2_item_4',
        ),
        migrations.RemoveField(
            model_name='match',
            name='p2_item_5',
        ),
        migrations.RemoveField(
            model_name='match',
            name='p2_item_6',
        ),
        migrations.RemoveField(
            model_name='match',
            name='p2_name',
        ),
        migrations.RemoveField(
            model_name='match',
            name='p2_win_status',
        ),
        migrations.CreateModel(
            name='Build',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('queue', models.IntegerField()),
                ('player_name', models.CharField(max_length=80)),
                ('duel_tier', models.IntegerField()),
                ('winner', models.BooleanField()),
                ('active_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='active_1', to='pages.Item')),
                ('active_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='active_2', to='pages.Item')),
                ('god', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='god', to='pages.God')),
                ('item_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_1', to='pages.Item')),
                ('item_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_2', to='pages.Item')),
                ('item_3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_3', to='pages.Item')),
                ('item_4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_4', to='pages.Item')),
                ('item_5', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_5', to='pages.Item')),
                ('item_6', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_6', to='pages.Item')),
                ('opponent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opponent', to='pages.God')),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='p1_build',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='p1_build', to='pages.Build'),
        ),
        migrations.AddField(
            model_name='match',
            name='p2_build',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='p2_build', to='pages.Build'),
        ),
    ]