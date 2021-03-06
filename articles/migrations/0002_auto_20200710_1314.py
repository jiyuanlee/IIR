# Generated by Django 2.2.9 on 2020-07-10 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name_plural': 'Articles'},
        ),
        migrations.AddField(
            model_name='articles',
            name='title',
            field=models.CharField(default=None, max_length=9999),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='articles',
            name='article_id_doi',
            field=models.CharField(max_length=9999),
        ),
        migrations.AlterField(
            model_name='articles',
            name='article_subject',
            field=models.CharField(max_length=9999),
        ),
        migrations.AlterField(
            model_name='articles',
            name='article_title',
            field=models.CharField(max_length=9999),
        ),
        migrations.AlterField(
            model_name='articles',
            name='contrib_given_names',
            field=models.CharField(max_length=9999),
        ),
        migrations.AlterField(
            model_name='articles',
            name='contrib_surname',
            field=models.CharField(max_length=9999),
        ),
        migrations.AlterField(
            model_name='articles',
            name='journal_title',
            field=models.CharField(max_length=9999),
        ),
        migrations.AlterField(
            model_name='articles',
            name='kwd',
            field=models.CharField(max_length=9999),
        ),
        migrations.AlterField(
            model_name='articles',
            name='ref_list_article_title',
            field=models.CharField(max_length=9999),
        ),
        migrations.AlterField(
            model_name='articles',
            name='ref_list_citation_given_names',
            field=models.CharField(max_length=9999),
        ),
        migrations.AlterField(
            model_name='articles',
            name='ref_list_citation_surname',
            field=models.CharField(max_length=9999),
        ),
        migrations.AlterField(
            model_name='articles',
            name='ref_list_source',
            field=models.CharField(max_length=9999),
        ),
        migrations.AlterField(
            model_name='articles',
            name='sec_display_objects_title',
            field=models.CharField(max_length=9999),
        ),
        migrations.AlterField(
            model_name='articles',
            name='sec_methods_title',
            field=models.CharField(max_length=9999),
        ),
        migrations.AlterField(
            model_name='articles',
            name='sec_title',
            field=models.CharField(max_length=9999),
        ),
    ]
