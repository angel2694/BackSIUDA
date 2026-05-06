from django.contrib import admin
from .models import Request, RequestDetail

class RequestDetailInline(admin.TabularInline):
    model = RequestDetail
    extra = 1

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('code', 'area', 'user', 'status', 'created')
    list_filter = ('status', 'area')
    search_fields = ('code',)
    readonly_fields = ('created', 'updated')
    inlines = [RequestDetailInline]
