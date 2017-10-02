from django.contrib import admin

# Register your models here.
from .models import project, information, teams, list_of_keys

admin.site.register(project)
admin.site.register(information)
admin.site.register(teams)
admin.site.register(list_of_keys)