from django.contrib import admin
from .models import Link

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']

    def get_readonly_fields(self, request, obj=None):
        # Check if the user belongs to the "Staff" group.
        if request.user.groups.filter(name="Staff").exists():
            return ['key', 'name']
        else:
            return ['created', 'updated']
        

admin.site.register(Link, LinkAdmin)