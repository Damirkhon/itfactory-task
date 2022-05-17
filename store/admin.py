from django.contrib import admin
from .models import Employee, Store, Visit


class EmployeeAdmin(admin.ModelAdmin):
    search_fields = ["name"]


class StoreAdmin(admin.ModelAdmin):
    search_fields = ["name"]


class VisitAdmin(admin.ModelAdmin):
    list_display = ("store", "get_employee", "time")
    search_fields = ["store__name", "store__employee__name"]
    readonly_fields = ("time", "store", "latitude", "longtitude")

    @admin.display(ordering="store_employee", description="Employee")
    def get_employee(self, obj):
        return obj.store.employee

    def has_add_permission(self, request, obj=None):
        return False


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Visit, VisitAdmin)
