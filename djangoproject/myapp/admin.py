from django.contrib import admin
from .models import Support
# Register your models here.

class SupportAdmin(admin.ModelAdmin):
   list_display = ['type','supporter','money','status']

admin.site.register(Support, SupportAdmin)