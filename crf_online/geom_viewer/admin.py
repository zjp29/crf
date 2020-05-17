from django.contrib.gis import admin
from .models import  *


@admin.register(tblResource)
class ResourceAdmin(admin.OSMGeoAdmin):
    list_display = ('pnumber','resourcenotes','resourcedisclose','age','info','trinomial')


@admin.register(tblInventory)
class InventoryAdmin(admin.OSMGeoAdmin):
    list_display = ('reportnum', 'disclosure', 'shp','pdf')

@admin.register(nwic_ccd_crf)
class NwicAdmin(admin.OSMGeoAdmin):
    list_display = ('pnumber', 'disclosure', 'status','trinomial')


admin.site.register(resource_points,admin.OSMGeoAdmin)





admin.site.site_header = 'CRF Administration'
