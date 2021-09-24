# Generated by Django 3.1.7 on 2021-09-22 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cus_app', '0005_auto_20210922_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='diagnostic',
            field=models.CharField(default='not done', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='medicine_sold',
            field=models.CharField(default='not done', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='surgical_or_consultation',
            field=models.CharField(default='not done', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='visit_for_Queries',
            field=models.CharField(default='not done', max_length=500, null=True),
        ),
    ]
