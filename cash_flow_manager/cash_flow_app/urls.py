from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_record, name='create_record'),
    path('edit/<int:pk>/', views.edit_record, name='edit_record'),
    path('delete/<int:pk>/', views.delete_record, name='delete_record'),
    path('dictionaries/', views.manage_dictionaries, name='manage_dictionaries'),

    # Статусы
    path('dictionaries/status/create/', views.create_status, name='create_status'),
    path('dictionaries/status/edit/<int:pk>/', views.edit_status, name='edit_status'),
    path('dictionaries/status/delete/<int:pk>/', views.delete_status, name='delete_status'),

    # Типы
    path('dictionaries/type/create/', views.create_type, name='create_type'),
    path('dictionaries/type/edit/<int:pk>/', views.edit_type, name='edit_type'),
    path('dictionaries/type/delete/<int:pk>/', views.delete_type, name='delete_type'),

    # Категории
    path('dictionaries/category/create/', views.create_category, name='create_category'),
    path('dictionaries/category/edit/<int:pk>/', views.edit_category, name='edit_category'),
    path('dictionaries/category/delete/<int:pk>/', views.delete_category, name='delete_category'),

    # Подкатегории
    path('dictionaries/subcategory/create/', views.create_subcategory, name='create_subcategory'),
    path('dictionaries/subcategory/edit/<int:pk>/', views.edit_subcategory, name='edit_subcategory'),
    path('dictionaries/subcategory/delete/<int:pk>/', views.delete_subcategory, name='delete_subcategory'),

    # API для динамической загрузки
    path('api/categories/', views.get_categories, name='get_categories'),
    path('api/subcategories/', views.get_subcategories, name='get_subcategories'),
]