# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models


class nwic_ccd_crf(models.Model):
    pnumber = models.CharField(max_length=11)
    status = models.TextField(blank=True, null=True)
    disclosure = models.TextField(blank=True, null=True)
    shp = models.BooleanField(blank=True, null=True)
    pdf = models.BooleanField(blank=True, null=True)
    pdf_path = models.TextField(blank=True, null=True)
    trinomial = models.TextField(blank=True, null=True)
    id = models.AutoField(primary_key=True)
    primco = models.IntegerField(blank=True, null=True)
    primno = models.IntegerField(blank=True, null=True)
    trinh = models.CharField(max_length=255, blank=True, null=True)
    resourcename = models.CharField(max_length=255, blank=True, null=True)
    restype = models.CharField(max_length=255, blank=True, null=True)
    resourcecollections = models.CharField(max_length=255, blank=True, null=True)
    accessionno = models.CharField(max_length=255, blank=True, null=True)
    collectionsfacility = models.CharField(max_length=200, blank=True, null=True)
    age = models.CharField(max_length=255, blank=True, null=True)
    info = models.CharField(max_length=255, blank=True, null=True)
    resourcenotes = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        db_table = 'nwic_ccd_crf'


class report_aprxloc(models.Model):
    id = models.AutoField(primary_key=True)
    geom = models.MultiPolygonField(srid=3310, blank=True, null=True)
    docco = models.IntegerField(db_column='DocCo', blank=True, null=True)  # Field name made lowercase.
    docno = models.IntegerField(db_column='DocNo', blank=True, null=True)  # Field name made lowercase.
    label = models.CharField(db_column='Label', max_length=25, blank=True, null=True) # Field name made lowercase.
    otherid = models.CharField(db_column='OtherID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    docsource = models.CharField(db_column='DocSource', max_length=25, blank=True, null=True)  # Field name made lowercase.
    digsource = models.CharField(db_column='DigSource', max_length=25, blank=True, null=True)  # Field name made lowercase.
    reportnum = models.ForeignKey('tblInventory', models.DO_NOTHING, db_column='ReportNum', blank=True, null=True,to_field="reportnum")  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    confidential = models.CharField(db_column='Confidential', max_length=3, blank=True, null=True)  # Field name made lowercase.
    hyperlink = models.CharField(db_column='Hyperlink', max_length=255, blank=True, null=True)  # Field name made lowercase.
    shape_length = models.FloatField(db_column='SHAPE_Length', blank=True, null=True)  # Field name made lowercase.
    shape_area = models.FloatField(db_column='SHAPE_Area', blank=True, null=True)  # Field name made lowercase.
    digorg = models.CharField(db_column='DigOrg', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'report_aprxloc'


class report_cfmou(models.Model):
    id = models.AutoField(primary_key=True)
    geom = models.MultiPolygonField(srid=3310, blank=True, null=True)
    docco = models.IntegerField(db_column='DocCo', blank=True, null=True)  # Field name made lowercase.
    docno = models.IntegerField(db_column='DocNo', blank=True, null=True)  # Field name made lowercase.
    label = models.CharField(db_column='Label', max_length=25, blank=True, null=True)  # Field name made lowercase.
    otherid = models.CharField(db_column='OtherID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    docsource = models.CharField(db_column='DocSource', max_length=25, blank=True, null=True)  # Field name made lowercase.
    digsource = models.CharField(db_column='DigSource', max_length=25, blank=True, null=True)  # Field name made lowercase.
    reportnum = models.ForeignKey('tblInventory', models.DO_NOTHING, db_column='ReportNum', blank=True, null=True,to_field="reportnum")  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hyperlink = models.CharField(db_column='Hyperlink', max_length=250, blank=True, null=True)  # Field name made lowercase.
    shape_length = models.FloatField(db_column='SHAPE_Length', blank=True, null=True)  # Field name made lowercase.
    shape_area = models.FloatField(db_column='SHAPE_Area', blank=True, null=True)  # Field name made lowercase.
    digorg = models.CharField(db_column='DigOrg', max_length=255, blank=True, null=True)  # Field name made lowercase.
    confidential = models.CharField(db_column='Confidential', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'report_cfmou'


class report_lines(models.Model):
    id = models.AutoField(primary_key=True)
    geom = models.MultiLineStringField(srid=3310, blank=True, null=True)
    docco = models.IntegerField(db_column='DocCo', blank=True, null=True)  # Field name made lowercase.
    docno = models.IntegerField(db_column='DocNo', blank=True, null=True)  # Field name made lowercase.
    label = models.CharField(db_column='Label', max_length=25, blank=True, null=True)  # Field name made lowercase.
    otherid = models.CharField(db_column='OtherID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    docsource = models.CharField(db_column='DocSource', max_length=25, blank=True, null=True)  # Field name made lowercase.
    digsource = models.CharField(db_column='DigSource', max_length=25, blank=True, null=True)  # Field name made lowercase.
    reportnum = models.ForeignKey('tblInventory', models.DO_NOTHING, db_column='ReportNum', blank=True, null=True,to_field="reportnum")  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hyperlink = models.CharField(db_column='Hyperlink', max_length=250, blank=True, null=True)  # Field name made lowercase.
    shape_length = models.FloatField(db_column='SHAPE_Length', blank=True, null=True)  # Field name made lowercase.
    digorg = models.CharField(db_column='DigOrg', max_length=255, blank=True, null=True)  # Field name made lowercase.
    confidential = models.CharField(db_column='Confidential', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'report_lines'


class report_other(models.Model):
    id = models.AutoField(primary_key=True)
    geom = models.MultiPolygonField(srid=3310, blank=True, null=True)
    docco = models.IntegerField(db_column='DocCo', blank=True, null=True)  # Field name made lowercase.
    docno = models.IntegerField(db_column='DocNo', blank=True, null=True)  # Field name made lowercase.
    label = models.CharField(db_column='Label', max_length=25, blank=True, null=True)  # Field name made lowercase.
    otherid = models.CharField(db_column='OtherID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    docsource = models.CharField(db_column='DocSource', max_length=25, blank=True, null=True)  # Field name made lowercase.
    digsource = models.CharField(db_column='DigSource', max_length=25, blank=True, null=True)  # Field name made lowercase.
    reportnum = models.ForeignKey('tblInventory', models.DO_NOTHING, db_column='ReportNum', blank=True, null=True,to_field="reportnum")  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hyperlink = models.CharField(db_column='Hyperlink', max_length=250, blank=True, null=True)  # Field name made lowercase.
    shape_length = models.FloatField(db_column='Shape_Length', blank=True, null=True)  # Field name made lowercase.
    shape_area = models.FloatField(db_column='Shape_Area', blank=True, null=True)  # Field name made lowercase.
    digorg = models.CharField(db_column='DigOrg', max_length=255, blank=True, null=True)  # Field name made lowercase.
    confidential = models.CharField(db_column='Confidential', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'report_other'


class report_points(models.Model):
    id = models.AutoField(primary_key=True)
    geom = models.PointField(srid=3310, blank=True, null=True)
    docco = models.IntegerField(db_column='DocCo', blank=True, null=True)  # Field name made lowercase.
    docno = models.IntegerField(db_column='DocNo', blank=True, null=True)  # Field name made lowercase.
    label = models.CharField(db_column='Label', max_length=25, blank=True, null=True)  # Field name made lowercase.
    otherid = models.CharField(db_column='OtherID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    docsource = models.CharField(db_column='DocSource', max_length=25, blank=True, null=True)  # Field name made lowercase.
    digsource = models.CharField(db_column='DigSource', max_length=25, blank=True, null=True)  # Field name made lowercase.
    reportnum = models.ForeignKey('tblInventory', models.DO_NOTHING, db_column='ReportNum', blank=True, null=True,to_field="reportnum")  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hyperlink = models.CharField(db_column='Hyperlink', max_length=250, blank=True, null=True)  # Field name made lowercase.
    digorg = models.CharField(db_column='DigOrg', max_length=255, blank=True, null=True)  # Field name made lowercase.
    confidential = models.CharField(db_column='Confidential', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'report_points'


class report_polys(models.Model):
    id = models.AutoField(primary_key=True)
    geom = models.MultiPolygonField(srid=3310, blank=True, null=True)
    docco = models.IntegerField(db_column='DocCo', blank=True, null=True)  # Field name made lowercase.
    docno = models.IntegerField(db_column='DocNo', blank=True, null=True)  # Field name made lowercase.
    label = models.CharField(db_column='Label', max_length=25, blank=True, null=True)  # Field name made lowercase.
    otherid = models.CharField(db_column='OtherID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    docsource = models.CharField(db_column='DocSource', max_length=25, blank=True, null=True)  # Field name made lowercase.
    digsource = models.CharField(db_column='DigSource', max_length=25, blank=True, null=True)  # Field name made lowercase.
    reportnum = models.ForeignKey('tblInventory', models.DO_NOTHING, db_column='ReportNum', blank=True, null=True,to_field="reportnum")  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hyperlink = models.CharField(db_column='Hyperlink', max_length=250, blank=True, null=True)  # Field name made lowercase.
    shape_length = models.FloatField(db_column='Shape_Length', blank=True, null=True)  # Field name made lowercase.
    shape_area = models.FloatField(db_column='Shape_Area', blank=True, null=True)  # Field name made lowercase.
    digorg = models.CharField(db_column='DigOrg', max_length=255, blank=True, null=True)  # Field name made lowercase.
    confidential = models.CharField(db_column='Confidential', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'report_polys'


class report_restricted(models.Model):
    id = models.AutoField(primary_key=True)
    geom = models.MultiPolygonField(srid=3310, blank=True, null=True)
    docco = models.IntegerField(db_column='DocCo', blank=True, null=True)  # Field name made lowercase.
    docno = models.IntegerField(db_column='DocNo', blank=True, null=True)  # Field name made lowercase.
    label = models.CharField(db_column='Label', max_length=25, blank=True, null=True) # Field name made lowercase.
    otherid = models.CharField(db_column='OtherID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    docsource = models.CharField(db_column='DocSource', max_length=25, blank=True, null=True)  # Field name made lowercase.
    digsource = models.CharField(db_column='DigSource', max_length=25, blank=True, null=True)  # Field name made lowercase.
    reportnum = models.ForeignKey('tblInventory', models.DO_NOTHING, db_column='ReportNum', blank=True, null=True,to_field="reportnum")  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hyperlink = models.CharField(db_column='Hyperlink', max_length=250, blank=True, null=True)  # Field name made lowercase.
    shape_length = models.FloatField(db_column='SHAPE_Length', blank=True, null=True)  # Field name made lowercase.
    shape_area = models.FloatField(db_column='SHAPE_Area', blank=True, null=True)  # Field name made lowercase.
    digorg = models.CharField(db_column='DigOrg', max_length=255, blank=True, null=True)  # Field name made lowercase.
    confidential = models.CharField(db_column='Confidential', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'report_restricted'


class resource_aprxloc(models.Model):
    id = models.AutoField(primary_key=True)
    geom = models.MultiPolygonField(srid=3310, blank=True, null=True)
    primco = models.IntegerField(db_column='PrimCo', blank=True, null=True)  # Field name made lowercase.
    primno = models.IntegerField(db_column='PrimNo', blank=True, null=True)  # Field name made lowercase.
    trinno = models.IntegerField(db_column='TrinNo', blank=True, null=True)  # Field name made lowercase.
    label = models.ForeignKey('tblResource', models.DO_NOTHING, db_column='Label', blank=True, null=True,to_field="pnumber")  # Field name made lowercase.
    otherid = models.CharField(db_column='OtherID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    docsource = models.CharField(db_column='DocSource', max_length=1, blank=True, null=True)  # Field name made lowercase.
    digsource = models.CharField(db_column='DigSource', max_length=1, blank=True, null=True)  # Field name made lowercase.
    trinomial = models.CharField(db_column='Trinomial', max_length=11, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hyperlink = models.CharField(db_column='Hyperlink', max_length=250, blank=True, null=True)  # Field name made lowercase.
    shape_length = models.FloatField(db_column='SHAPE_Length', blank=True, null=True)  # Field name made lowercase.
    shape_area = models.FloatField(db_column='SHAPE_Area', blank=True, null=True)  # Field name made lowercase.
    digorg = models.CharField(db_column='DigOrg', max_length=255, blank=True, null=True)  # Field name made lowercase.
    confidential = models.CharField(db_column='Confidential', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'resource_aprxloc'


class resource_districts(models.Model):
    id = models.AutoField(primary_key=True)
    geom = models.MultiPolygonField(srid=3310, blank=True, null=True)
    primco = models.IntegerField(db_column='PrimCo', blank=True, null=True)  # Field name made lowercase.
    primno = models.IntegerField(db_column='PrimNo', blank=True, null=True)  # Field name made lowercase.
    trinno = models.IntegerField(db_column='TrinNo', blank=True, null=True)  # Field name made lowercase.
    label = models.ForeignKey('tblResource', models.DO_NOTHING, db_column='Label', blank=True, null=True,to_field="pnumber")  # Field name made lowercase.
    otherid = models.CharField(db_column='OtherID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    docsource = models.CharField(db_column='DocSource', max_length=25, blank=True, null=True)  # Field name made lowercase.
    digsource = models.CharField(db_column='DigSource', max_length=25, blank=True, null=True)  # Field name made lowercase.
    trinomial = models.CharField(db_column='Trinomial', max_length=11, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hyperlink = models.CharField(db_column='Hyperlink', max_length=250, blank=True, null=True)  # Field name made lowercase.
    shape_length = models.FloatField(db_column='SHAPE_Length', blank=True, null=True)  # Field name made lowercase.
    shape_area = models.FloatField(db_column='SHAPE_Area', blank=True, null=True)  # Field name made lowercase.
    confidential = models.CharField(db_column='Confidential', max_length=3, blank=True, null=True)  # Field name made lowercase.
    digorg = models.CharField(db_column='DigOrg', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'resource_districts'


class resource_lines(models.Model):
    id = models.AutoField(primary_key=True)
    geom = models.MultiLineStringField(srid=3310, blank=True, null=True)
    primco = models.IntegerField(db_column='PrimCo', blank=True, null=True)  # Field name made lowercase.
    primno = models.IntegerField(db_column='PrimNo', blank=True, null=True)  # Field name made lowercase.
    trinno = models.CharField(db_column='TrinNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    label = models.ForeignKey('tblResource', models.DO_NOTHING, db_column='Label', blank=True, null=True,to_field="pnumber")  # Field name made lowercase.
    otherid = models.CharField(db_column='OtherID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    docsource = models.CharField(db_column='DocSource', max_length=25, blank=True, null=True)  # Field name made lowercase.
    digsource = models.CharField(db_column='DigSource', max_length=25, blank=True, null=True)  # Field name made lowercase.
    trinomial = models.CharField(db_column='Trinomial', max_length=20, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hyperlink = models.CharField(db_column='Hyperlink', max_length=250, blank=True, null=True)  # Field name made lowercase.
    shape_length = models.FloatField(db_column='SHAPE_Length', blank=True, null=True)  # Field name made lowercase.
    confidential = models.CharField(db_column='Confidential', max_length=3, blank=True, null=True)  # Field name made lowercase.
    digorg = models.CharField(db_column='DigOrg', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'resource_lines'


class resource_points(models.Model):
    id = models.AutoField(primary_key=True)
    geom = models.PointField(srid=3310, blank=True, null=True)
    primco = models.IntegerField(db_column='PrimCo', blank=True, null=True)  # Field name made lowercase.
    primno = models.IntegerField(db_column='PrimNo', blank=True, null=True)  # Field name made lowercase.
    trinno = models.CharField(db_column='TrinNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    label = models.ForeignKey('tblResource', models.DO_NOTHING, db_column='Label', blank=True, null=True,to_field="pnumber")  # Field name made lowercase.
    otherid = models.CharField(db_column='OtherID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    docsource = models.CharField(db_column='DocSource', max_length=25, blank=True, null=True)  # Field name made lowercase.
    digsource = models.CharField(db_column='DigSource', max_length=25, blank=True, null=True)  # Field name made lowercase.
    trinomial = models.CharField(db_column='Trinomial', max_length=20, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hyperlink = models.CharField(db_column='Hyperlink', max_length=250, blank=True, null=True)  # Field name made lowercase.
    confidential = models.CharField(db_column='Confidential', max_length=3, blank=True, null=True)  # Field name made lowercase.
    digorg = models.CharField(db_column='DigOrg', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'resource_points'


class resource_polys(models.Model):
    id = models.AutoField(primary_key=True)
    geom = models.MultiPolygonField(srid=3310, blank=True, null=True)
    primco = models.IntegerField(db_column='PrimCo', blank=True, null=True)  # Field name made lowercase.
    primno = models.IntegerField(db_column='PrimNo', blank=True, null=True)  # Field name made lowercase.
    trinno = models.IntegerField(db_column='TrinNo', blank=True, null=True)  # Field name made lowercase.
    label = models.ForeignKey('tblResource', models.DO_NOTHING, db_column='Label', blank=True, null=True,to_field="pnumber")  # Field name made lowercase.
    otherid = models.CharField(db_column='OtherID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    docsource = models.CharField(db_column='DocSource', max_length=25, blank=True, null=True)  # Field name made lowercase.
    digsource = models.CharField(db_column='DigSource', max_length=25, blank=True, null=True)  # Field name made lowercase.
    trinomial = models.CharField(db_column='Trinomial', max_length=20, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hyperlink = models.CharField(db_column='Hyperlink', max_length=250, blank=True, null=True)  # Field name made lowercase.
    shape_length = models.FloatField(db_column='SHAPE_Length', blank=True, null=True)  # Field name made lowercase.
    shape_area = models.FloatField(db_column='SHAPE_Area', blank=True, null=True)  # Field name made lowercase.
    confidential = models.CharField(db_column='Confidential', max_length=3, blank=True, null=True)  # Field name made lowercase.
    digorg = models.CharField(db_column='DigOrg', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'resource_polys'


class resource_restricted(models.Model):
    id = models.AutoField(primary_key=True)
    geom = models.MultiPolygonField(srid=3310, blank=True, null=True)
    primco = models.IntegerField(db_column='PrimCo', blank=True, null=True)  # Field name made lowercase.
    primno = models.IntegerField(db_column='PrimNo', blank=True, null=True)  # Field name made lowercase.
    trinno = models.IntegerField(db_column='TrinNo', blank=True, null=True)  # Field name made lowercase.
    label = models.ForeignKey('tblResource', models.DO_NOTHING, db_column='Label', blank=True, null=True,to_field="pnumber")  # Field name made lowercase.
    otherid = models.CharField(db_column='OtherID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    docsource = models.CharField(db_column='DocSource', max_length=25, blank=True, null=True)  # Field name made lowercase.
    digsource = models.CharField(db_column='DigSource', max_length=25, blank=True, null=True)  # Field name made lowercase.
    trinomial = models.CharField(db_column='Trinomial', max_length=20, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hyperlink = models.CharField(db_column='Hyperlink', max_length=250, blank=True, null=True)  # Field name made lowercase.
    shape_length = models.FloatField(db_column='SHAPE_Length', blank=True, null=True)  # Field name made lowercase.
    shape_area = models.FloatField(db_column='SHAPE_Area', blank=True, null=True)  # Field name made lowercase.
    confidential = models.CharField(db_column='Confidential', max_length=3, blank=True, null=True)  # Field name made lowercase.
    digorg = models.CharField(db_column='DigOrg', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'resource_restricted'


class tblInvX(models.Model):
    id = models.AutoField(primary_key=True)
    objectid = models.BigIntegerField(db_column='OBJECTID', blank=True, null=True)  # Field name made lowercase.
    reportnum = models.ForeignKey('tblInventory', models.DO_NOTHING, db_column='ReportNum', blank=True, null=True,to_field="reportnum")  # Field name made lowercase.
    pnumber = models.CharField(db_column='PNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'tblInvX'


class tblInventory(models.Model):
    docno = models.CharField(db_column='DocNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    label = models.CharField(db_column='Label', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reportnum = models.CharField(db_column='ReportNum',  max_length=10,unique=True)  # Field name made lowercase.
    olddocno = models.CharField(db_column='OldDocNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inventorysize = models.CharField(db_column='InventorySize', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inventorysites = models.CharField(db_column='InventorySites', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inventoryinformals = models.CharField(db_column='InventoryInformals', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inventorycollections = models.CharField(db_column='InventoryCollections', max_length=255, blank=True, null=True)  # Field name made lowercase.
    disclosure = models.CharField(db_column='Disclosure', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cityear = models.CharField(db_column='CitYear', max_length=255, blank=True, null=True)  # Field name made lowercase.
    citmonth = models.CharField(db_column='CitMonth', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cittitle = models.CharField(db_column='CitTitle', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    citpublisher = models.CharField(db_column='CitPublisher', max_length=255, blank=True, null=True)  # Field name made lowercase.
    citpages = models.CharField(db_column='CitPages', max_length=255, blank=True, null=True)  # Field name made lowercase.
    citmaps = models.CharField(db_column='CitMaps', max_length=255, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    pdf = models.BooleanField(blank=True, null=True)
    shp = models.BooleanField(blank=True, null=True)
    id = models.AutoField(primary_key=True)

    class Meta:
        db_table = 'tblInventory'


class tblInventoryAddr(models.Model):
    id = models.AutoField(primary_key=True)
    reportnum = models.ForeignKey(tblInventory, models.DO_NOTHING, db_column='ReportNum', blank=True, null=True,to_field="reportnum")  # Field name made lowercase.
    streetnumber = models.CharField(db_column='StreetNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    streetname = models.CharField(db_column='StreetName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    streetsuffix = models.CharField(db_column='StreetSuffix', max_length=255, blank=True, null=True)  # Field name made lowercase.
    streetdirection = models.CharField(db_column='StreetDirection', max_length=255, blank=True, null=True)  # Field name made lowercase.
    streetaddress = models.CharField(db_column='StreetAddress', max_length=255, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=255, blank=True, null=True)  # Field name made lowercase.
    apn = models.CharField(db_column='APN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    zip = models.CharField(db_column='Zip', max_length=255, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'tblInventoryAddr'


class tblInventoryAuthor(models.Model):
    id = models.AutoField(primary_key=True)
    reportnum = models.ForeignKey(tblInventory, models.DO_NOTHING, db_column='ReportNum', blank=True, null=True,to_field="reportnum")  # Field name made lowercase.
    primaryauthor = models.CharField(db_column='PrimaryAuthor', max_length=500, blank=True, null=True)  # Field name made lowercase.
    secondaryauthor = models.CharField(db_column='SecondaryAuthor', max_length=500, blank=True, null=True)  # Field name made lowercase.
    multipleauthors = models.CharField(db_column='MultipleAuthors', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    docauthortext = models.CharField(db_column='DocAuthorText', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'tblInventoryAuthor'


class tblInventoryCnty(models.Model):
    id = models.AutoField(primary_key=True)
    reportnum = models.ForeignKey(tblInventory, models.DO_NOTHING, db_column='ReportNum', blank=True, null=True,to_field="reportnum")  # Field name made lowercase.
    countyname = models.CharField(db_column='CountyName', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'tblInventoryCnty'


class tblInventoryIdent(models.Model):
    id = models.AutoField(primary_key=True)
    reportnum = models.ForeignKey(tblInventory, models.DO_NOTHING, db_column='ReportNum', blank=True, null=True,to_field="reportnum")  # Field name made lowercase.
    identifiertype = models.CharField(db_column='IdentifierType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    identifier = models.CharField(db_column='Identifier', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'tblInventoryIdent'


class tblInventoryMaps(models.Model):
    id = models.AutoField(primary_key=True)
    reportnum = models.ForeignKey(tblInventory, models.DO_NOTHING, db_column='ReportNum', blank=True, null=True,to_field="reportnum")  # Field name made lowercase.
    quadname = models.CharField(db_column='QuadName', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'tblInventoryMaps'


class tblInventoryType(models.Model):
    id = models.AutoField(primary_key=True)
    reportnum = models.ForeignKey(tblInventory, models.DO_NOTHING, db_column='ReportNum', blank=True, null=True,to_field="reportnum")  # Field name made lowercase.
    reporttype = models.CharField(db_column='ReportType', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'tblInventoryType'


class tblInventoryXRef(models.Model):
    id = models.AutoField(primary_key=True)
    reportnum = models.ForeignKey(tblInventory, models.DO_NOTHING, db_column='ReportNum', blank=True, null=True,to_field="reportnum")  # Field name made lowercase.
    reportnum1 = models.CharField(db_column='ReportNum1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reltype = models.CharField(db_column='RelType', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'tblInventoryXRef'


class tblResX(models.Model):
    id = models.AutoField(primary_key=True)
    objectid = models.BigIntegerField(db_column='OBJECTID', blank=True, null=True)  # Field name made lowercase.
    snumber = models.CharField(db_column='SNumber', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pnumber = models.ForeignKey('Tblresource', models.DO_NOTHING, db_column='PNumber', blank=True, null=True,to_field="pnumber")  # Field name made lowercase.

    class Meta:
        db_table = 'tblResX'


class tblResource(models.Model):
    id = models.AutoField(primary_key=True)
    primco = models.IntegerField(db_column='PrimCo', blank=True, null=True)  # Field name made lowercase.
    primno = models.IntegerField(db_column='PrimNo', blank=True, null=True)  # Field name made lowercase.
    pnumber = models.CharField(db_column='PNumber', unique=True, max_length=11, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=255, blank=True, null=True)  # Field name made lowercase.
    trinno = models.CharField(db_column='TrinNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    trinh = models.CharField(db_column='TrinH', max_length=255, blank=True, null=True)  # Field name made lowercase.
    resourcename = models.CharField(db_column='ResourceName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    restype = models.CharField(db_column='ResType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    resourcedisclose = models.CharField(db_column='ResourceDisclose', max_length=255, blank=True, null=True)  # Field name made lowercase.
    resourcecollections = models.CharField(db_column='ResourceCollections', max_length=255, blank=True, null=True)  # Field name made lowercase.
    accessionno = models.CharField(db_column='AccessionNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    collectionsfacility = models.CharField(db_column='CollectionsFacility', max_length=200, blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(db_column='Age', max_length=255, blank=True, null=True)  # Field name made lowercase.
    info = models.CharField(db_column='Info', max_length=255, blank=True, null=True)  # Field name made lowercase.
    resourcenotes = models.CharField(db_column='ResourceNotes', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    trinomial = models.CharField(db_column='Trinomial', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pdf = models.BooleanField(db_column='pdf',blank=True, null=True)
    shp = models.BooleanField(db_column='shp',blank=True, null=True)

    class Meta:
        db_table = 'tblResource'


class tblResourceAddr(models.Model):
    id = models.AutoField(primary_key=True)
    objectid = models.BigIntegerField(db_column='OBJECTID', blank=True, null=True)  # Field name made lowercase.
    pnumber = models.ForeignKey(tblResource, models.DO_NOTHING, db_column='PNumber', blank=True, null=True,to_field="pnumber")  # Field name made lowercase.
    streetnumber = models.CharField(db_column='StreetNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    streetname = models.CharField(db_column='StreetName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    streetsuffix = models.CharField(db_column='StreetSuffix', max_length=255, blank=True, null=True)  # Field name made lowercase.
    streetdirection = models.CharField(db_column='StreetDirection', max_length=255, blank=True, null=True)  # Field name made lowercase.
    streetaddress = models.CharField(db_column='StreetAddress', max_length=255, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=255, blank=True, null=True)  # Field name made lowercase.
    apn = models.CharField(db_column='APN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    zip = models.CharField(db_column='Zip', max_length=255, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'tblResourceAddr'


class tblResourceAttrib(models.Model):
    id = models.AutoField(primary_key=True)
    objectid = models.BigIntegerField(db_column='OBJECTID', blank=True, null=True)  # Field name made lowercase.
    pnumber = models.ForeignKey(tblResource, models.DO_NOTHING, db_column='PNumber', blank=True, null=True,to_field="pnumber")  # Field name made lowercase.
    attribid = models.CharField(db_column='AttribID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    attribnotes = models.CharField(db_column='AttribNotes', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'tblResourceAttrib'


class tblResourceEvents(models.Model):
    id = models.AutoField(primary_key=True)
    objectid = models.BigIntegerField(db_column='OBJECTID', blank=True, null=True)  # Field name made lowercase.
    pnumber = models.ForeignKey(tblResource, models.DO_NOTHING, db_column='PNumber', blank=True, null=True,to_field="pnumber")  # Field name made lowercase.
    recdate = models.CharField(db_column='RecDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    recorder = models.CharField(db_column='Recorder', max_length=255, blank=True, null=True)  # Field name made lowercase.
    affiliation = models.CharField(db_column='Affiliation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    recnote = models.CharField(db_column='RecNote', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'tblResourceEvents'


class tblResourceIdent(models.Model):
    id = models.AutoField(primary_key=True)
    objectid = models.BigIntegerField(db_column='OBJECTID', blank=True, null=True)  # Field name made lowercase.
    pnumber = models.ForeignKey(tblResource, models.DO_NOTHING, db_column='PNumber', blank=True, null=True,to_field="pnumber")  # Field name made lowercase.
    identifiertype = models.CharField(db_column='IdentifierType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    identifier = models.CharField(db_column='Identifier', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'tblResourceIdent'


class tblResourceMaps(models.Model):
    id = models.AutoField(primary_key=True)
    objectid = models.BigIntegerField(db_column='OBJECTID', blank=True, null=True)  # Field name made lowercase.
    pnumber = models.ForeignKey(tblResource, models.DO_NOTHING, db_column='PNumber', blank=True, null=True,to_field="pnumber")  # Field name made lowercase.
    quadname = models.CharField(db_column='QuadName', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'tblResourceMaps'


class tblResourcePLSS(models.Model):
    id = models.AutoField(primary_key=True)
    objectid = models.BigIntegerField(db_column='OBJECTID', blank=True, null=True)  # Field name made lowercase.
    pnumber = models.ForeignKey(tblResource, models.DO_NOTHING, db_column='PNumber', blank=True, null=True,to_field="pnumber")  # Field name made lowercase.
    basemer = models.CharField(db_column='BaseMer', max_length=500, blank=True, null=True)  # Field name made lowercase.
    tnumber = models.CharField(db_column='TNumber', max_length=500, blank=True, null=True)  # Field name made lowercase.
    tdirection = models.CharField(db_column='TDirection', max_length=500, blank=True, null=True)  # Field name made lowercase.
    rnumber = models.CharField(db_column='RNumber', max_length=500, blank=True, null=True)  # Field name made lowercase.
    rdirection = models.CharField(db_column='RDirection', max_length=500, blank=True, null=True)  # Field name made lowercase.
    qqsec = models.CharField(db_column='QQSec', max_length=500, blank=True, null=True)  # Field name made lowercase.
    qsec = models.CharField(db_column='QSec', max_length=500, blank=True, null=True)  # Field name made lowercase.
    section = models.CharField(db_column='Section', max_length=500, blank=True, null=True)  # Field name made lowercase.
    grant = models.CharField(db_column='Grant', max_length=500, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'tblResourcePLSS'


class tblResourceUTM(models.Model):
    id = models.AutoField(primary_key=True)
    objectid = models.BigIntegerField(db_column='OBJECTID', blank=True, null=True)  # Field name made lowercase.
    pnumber = models.ForeignKey(tblResource, models.DO_NOTHING, db_column='PNumber', blank=True, null=True,to_field="pnumber")  # Field name made lowercase.
    utmdatum = models.CharField(db_column='UTMDatum', max_length=255, blank=True, null=True)  # Field name made lowercase.
    utmzone = models.CharField(db_column='UTMZone', max_length=255, blank=True, null=True)  # Field name made lowercase.
    utmeasting = models.CharField(db_column='UTMEasting', max_length=255, blank=True, null=True)  # Field name made lowercase.
    utmnorthing = models.CharField(db_column='UTMNorthing', max_length=255, blank=True, null=True)  # Field name made lowercase.
    utmtext = models.CharField(db_column='UTMText', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'tblResourceUTM'


class tblResourceXRef(models.Model):
    id = models.AutoField(primary_key=True)
    objectid = models.BigIntegerField(db_column='OBJECTID', blank=True, null=True)  # Field name made lowercase.
    pnumber = models.ForeignKey(tblResource, models.DO_NOTHING, db_column='PNumber', blank=True, null=True,to_field="pnumber")  # Field name made lowercase.
    pnumber1 = models.CharField(db_column='PNumber1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reltype = models.CharField(db_column='RelType', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'tblResourceXRef'
