from django.contrib import admin
from .models import *



class AdminByke(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class ScooterAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}



admin.site.register(Category,CategoryAdmin)
admin.site.register(Byke,AdminByke)
admin.site.register(Scooter, ScooterAdmin)
admin.site.register(Img)