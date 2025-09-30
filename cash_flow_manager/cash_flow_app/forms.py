from django import forms
from .models import CashFlowRecord, Status, Type, Category, SubCategory


class CashFlowForm(forms.ModelForm):
    class Meta:
        model = CashFlowRecord
        fields = ['date', 'status', 'type', 'category', 'subcategory', 'amount', 'comment']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control', 'id': 'type-select'}),
            'category': forms.Select(attrs={'class': 'form-control', 'id': 'category-select'}),
            'subcategory': forms.Select(attrs={'class': 'form-control', 'id': 'subcategory-select'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'date': 'Дата операции',
            'status': 'Статус',
            'type': 'Тип операции',
            'category': 'Категория',
            'subcategory': 'Подкатегория',
            'amount': 'Сумма (руб.)',
            'comment': 'Комментарий',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Устанавливаем начальные значения для выпадающих списков
        if 'type' in self.data:
            try:
                type_id = int(self.data.get('type'))
                self.fields['category'].queryset = Category.objects.filter(type_id=type_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['category'].queryset = Category.objects.filter(type=self.instance.type)

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = SubCategory.objects.filter(category_id=category_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['subcategory'].queryset = SubCategory.objects.filter(category=self.instance.category)


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Название статуса',
        }


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Название типа',
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'type']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Название категории',
            'type': 'Тип операции',
        }


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['name', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Название подкатегории',
            'category': 'Категория',
        }