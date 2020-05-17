from django.contrib.gis import admin
from .models import NwicCcdCrf, Tblinventory, Tblresource, ResourceLines, ReportLines


@admin.register(NwicCcdCrf)
class ResourceAdmin(admin.GeoModelAdmin):
    list_display = ('pnumber', 'disclosure', 'shp','pdf')


admin.site.register(Tblinventory, admin.GeoModelAdmin)
admin.site.register(Tblresource, admin.GeoModelAdmin)
admin.site.register(ResourceLines, admin.GeoModelAdmin)
admin.site.register(ReportLines, admin.GeoModelAdmin)

admin.site.site_header = 'CRF Administration'