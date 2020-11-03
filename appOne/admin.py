from django.contrib import admin
from .models import Setting, ContactMessage


# Register your models here.
class SettingsAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'update_at', 'status']


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'message', 'update_at', 'status']
    readonly_fields = ('name', 'subject', 'email', 'message')
    list_filter = ['status']


admin.site.register(Setting, SettingsAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
