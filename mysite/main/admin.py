from django.contrib import admin
from .models import G_Logo, Soc, Category, SubCategory, Brand, Features_Item, HomeSlider, HomeSliderActive,Contact

# Register your models here.

admin.site.register(G_Logo)
admin.site.register(Soc)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Brand)
admin.site.register(HomeSliderActive)
admin.site.register(HomeSlider)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']
    list_display_links = ['id', 'name', 'email']
    search_fields = ['name', 'email']

@admin.register(Features_Item)
class Features_ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
    list_display_links = ['name']
    search_fields = ['id', 'name', 'price']