from django.contrib import admin
from .models import Link


class LinkAdmin(admin.ModelAdmin):
    search_fields = ('name',)

    def get_readonly_fields(self, request, obj: None):
        if request.user.groups.filter(name="Personal").exists():
            return ("key", "name")
        else:
            return ("created", "updated")


admin.site.register(Link, LinkAdmin)
