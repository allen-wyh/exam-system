# Generated by Django 2.2.12 on 2020-06-18 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competitionqainfo',
            name='qa_id',
            field=models.IntegerField(blank=True, db_index=True, help_text='QA 唯一标识', null=True, verbose_name='问题id'),
        ),
    ]
