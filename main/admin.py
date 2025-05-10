from django.contrib import admin
from . import models
@admin.register(models.HomeSlider)
class HomeSliderAdmin(admin.ModelAdmin):
    list_display = ("heading", "button_text", "order", "is_active")
    list_editable = ("order", "is_active")
    search_fields = ("heading", "subheading")

class ProjectImageInline(admin.TabularInline):
    model = models.ProjectImage
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]

admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.Blog)
admin.site.register(models.Contact)
admin.site.register(models.Announcement)
admin.site.register(models.Category)