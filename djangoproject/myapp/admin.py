from django.contrib import admin
from .models import Support
# Register your models here.

@admin.register(Support)
class SupportAdmin(admin.ModelAdmin):
   list_display = ['type','user','supporter','money','status']
   list_editable = ['status']
