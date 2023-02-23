from django.contrib import admin

# Register your models here.
from .models import Host

class ContactAdmin(admin.ModelAdmin):
        list_display = ('name', 'email', 'phone', 'address', 'image')

admin.site.register(Host, ContactAdmin)
