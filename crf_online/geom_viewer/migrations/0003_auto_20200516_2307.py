# Generated by Django 3.0.3 on 2020-05-17 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geom_viewer', '0002_auto_20200516_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report_aprxloc',
            name='label',
            field=models.CharField(blank=True, db_column='Label', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='report_aprxloc',
            name='reportnum',
            field=models.ForeignKey(blank=True, db_column='ReportNum', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='geom_viewer.tblInventory', to_field='reportnum'),
        ),
    ]
