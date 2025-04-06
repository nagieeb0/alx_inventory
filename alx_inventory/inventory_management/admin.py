from django.contrib import admin
from .models import Category, InventoryItem, InventoryChangeLog

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'price', 'category', 'user', 'last_updated')
    list_filter = ('category', 'user')
    search_fields = ('name', 'description')

@admin.register(InventoryChangeLog)
class InventoryChangeLogAdmin(admin.ModelAdmin):
    list_display = ('item', 'changed_by', 'old_quantity', 'new_quantity', 'change_date')
    list_filter = ('changed_by', 'change_date')
    search_fields = ('item__name',)