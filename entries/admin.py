from django.contrib import admin
from .models import Entry



@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('entry_title', 'image')


