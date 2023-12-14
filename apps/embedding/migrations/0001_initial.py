# Generated by Django 4.1.10 on 2023-12-14 04:11

import common.field.vector_field
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dataset', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Embedding',
            fields=[
                ('id', models.CharField(max_length=128, primary_key=True, serialize=False, verbose_name='主键id')),
                ('source_id', models.CharField(max_length=128, verbose_name='资源id')),
                ('source_type', models.CharField(choices=[('0', '问题'), ('1', '段落')], default='0', max_length=5, verbose_name='资源类型')),
                ('is_active', models.BooleanField(default=True, max_length=1, verbose_name='是否可用')),
                ('embedding', common.field.vector_field.VectorField(verbose_name='向量')),
                ('star_num', models.IntegerField(default=0, verbose_name='点赞数量')),
                ('trample_num', models.IntegerField(default=0, verbose_name='点踩数量')),
                ('dataset', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='dataset.dataset', verbose_name='文档关联')),
                ('document', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='dataset.document', verbose_name='文档关联')),
                ('paragraph', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='dataset.paragraph', verbose_name='段落关联')),
            ],
            options={
                'db_table': 'embedding',
                'unique_together': {('source_id', 'source_type')},
            },
        ),
    ]
