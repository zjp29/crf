from django.contrib.gis import admin
from .models import NwicCcdCrf, Tblinventory, Tblresource, ResourceLines, ReportLines


admin.site.register(NwicCcdCrf, admin.GeoModelAdmin)
admin.site.register(Tblinventory, admin.GeoModelAdmin)
admin.site.register(Tblresource, admin.GeoModelAdmin)
admin.site.register(ResourceLines, admin.GeoModelAdmin)
admin.site.register(ReportLines, admin.GeoModelAdmin)

admin.site.site_header = 'CRF Administration'

