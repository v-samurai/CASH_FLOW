from django.contrib import admin
from .models import Status, Type, Category, SubCategory, CashFlowRecord

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'type']
    list_filter = ['type']
    search_fields = ['name']

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    list_filter = ['category']
    search_fields = ['name']

@admin.register(CashFlowRecord)
class CashFlowRecordAdmin(admin.ModelAdmin):
    list_display = ['date', 'status', 'type', 'category', 'subcategory', 'amount']
    list_filter = ['date', 'status', 'type', 'category']
    search_fields = ['comment']
    readonly_fields = ['created_at', 'updated_at']