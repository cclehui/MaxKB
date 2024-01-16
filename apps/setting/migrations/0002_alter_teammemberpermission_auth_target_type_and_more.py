# Generated by Django 4.1.10 on 2023-12-28 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammemberpermission',
            name='auth_target_type',
            field=models.CharField(choices=[('DATASET', '数据集'), ('APPLICATION', '应用')], default='DATASET', max_length=128, verbose_name='授权目标'),
        ),
        migrations.AlterField(
            model_name='teammemberpermission',
            name='target',
            field=models.UUIDField(verbose_name='数据集/应用id'),
        ),
    ]