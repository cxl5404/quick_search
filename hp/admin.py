from django.contrib import admin

# Register your models here.
from .models import Tranceiver, Switch_100M,Switch_1G, Switch_10G
from import_export.admin import ImportExportModelAdmin


class TAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Tranceiver,TAdmin)
admin.site.register(Switch_100M,TAdmin)
admin.site.register(Switch_1G,TAdmin)
admin.site.register(Switch_10G,TAdmin)