from django.contrib import admin
from .models import saveData

# Register your models here.

class saveDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'key', 'user','created_on', 'updated_on']
    list_filter = ['key', 'id']
    search_fields = ['key', 'id']

    
admin.site.register(saveData, saveDataAdmin)
