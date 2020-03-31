from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import alumni,our_gems,gallery,notice_events,committee,staff
# Register your models here.

@admin.register(alumni)
class AlumniAdmin(ImportExportModelAdmin):
    pass

@admin.register(our_gems)
class AlumniAdmin(ImportExportModelAdmin):
    pass

@admin.register(gallery)
class galleryAdmin(ImportExportModelAdmin):
    pass

@admin.register(notice_events)
class notice_eventsAdmin(ImportExportModelAdmin):
    pass

@admin.register(staff)
class staffAdmin(ImportExportModelAdmin):
    pass

@admin.register(committee)
class committeeAdmin(ImportExportModelAdmin):
    pass
