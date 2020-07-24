# Generated by Django 2.2.9 on 2020-07-11 04:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20200710_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='ref_list',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='articles',
            name='aff_label',
            field=models.CharField(max_length=9999),
        ),
        migrations.AlterField(
            model_name='articles',
            name='article_id_pmc',
            field=models.CharField(max_length=9999),
        ),
        migrations.AlterField(
            model_name='articles',
            name='copyright_statement',
            field=models.CharField(max_length=9999),
        ),
        migrations.AlterField(
            model_name='articles',
            name='journal_id',
            field=models.CharField(max_length=9999),
        ),
        migrations.AlterField(
            model_name='articles',
            name='publisher_loc',
            field=models.CharField(max_length=9999),
        ),
        migrations.AlterField(
            model_name='articles',
            name='publisher_name',
            field=models.CharField(max_length=9999),
        ),
    ]