from django.contrib import admin

from .models import Ingredients, Recipes, Tag
from import_export import resources
from import_export.admin import ImportExportModelAdmin

@admin.register(Recipes)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'author',
    )
    list_filter = ('author', 'name', 'tags',)

class IngredientsResource(resources.ModelResource):

    class Meta:
        model = Ingredients


class IngredientsAdmin(ImportExportModelAdmin):
    resource_classes = [IngredientsResource]
    list_display = (
        'name',
        'measurement_unit',
    )
    search_fields = ('name',)
    list_filter = ('measurement_unit',)


admin.site.register(Tag)

admin.site.register(Ingredients, IngredientsAdmin)
