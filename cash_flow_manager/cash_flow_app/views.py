from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator
from .models import CashFlowRecord, Status, Type, Category, SubCategory
from .forms import CashFlowForm, StatusForm, TypeForm, CategoryForm, SubCategoryForm


def index(request):
    records = CashFlowRecord.objects.all().select_related('status', 'type', 'category', 'subcategory')

    # Фильтрация
    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')
    status_id = request.GET.get('status')
    type_id = request.GET.get('type')
    category_id = request.GET.get('category')
    subcategory_id = request.GET.get('subcategory')

    if date_from:
        records = records.filter(date__gte=date_from)
    if date_to:
        records = records.filter(date__lte=date_to)
    if status_id:
        records = records.filter(status_id=status_id)
    if type_id:
        records = records.filter(type_id=type_id)
    if category_id:
        records = records.filter(category_id=category_id)
    if subcategory_id:
        records = records.filter(subcategory_id=subcategory_id)

    # Пагинация
    paginator = Paginator(records, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'statuses': Status.objects.all(),
        'types': Type.objects.all(),
        'categories': Category.objects.all(),
        'subcategories': SubCategory.objects.all(),
        'filters': {
            'date_from': date_from,
            'date_to': date_to,
            'status': status_id,
            'type': type_id,
            'category': category_id,
            'subcategory': subcategory_id,
        }
    }

    return render(request, 'cash_flow_app/index.html', context)


def create_record(request):
    if request.method == 'POST':
        form = CashFlowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CashFlowForm()

    return render(request, 'cash_flow_app/record_form.html', {'form': form, 'title': 'Создать запись'})


def edit_record(request, pk):
    record = get_object_or_404(CashFlowRecord, pk=pk)

    if request.method == 'POST':
        form = CashFlowForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CashFlowForm(instance=record)

    return render(request, 'cash_flow_app/record_form.html', {'form': form, 'title': 'Редактировать запись'})


def delete_record(request, pk):
    record = get_object_or_404(CashFlowRecord, pk=pk)
    record.delete()
    return redirect('index')


def manage_dictionaries(request):
    context = {
        'statuses': Status.objects.all(),
        'types': Type.objects.all(),
        'categories': Category.objects.all(),
        'subcategories': SubCategory.objects.all(),
    }
    return render(request, 'cash_flow_app/dictionaries.html', context)


def create_status(request):
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_dictionaries')
    else:
        form = StatusForm()

    return render(request, 'cash_flow_app/dictionary_form.html', {
        'form': form,
        'title': 'Добавить статус',
        'back_url': 'manage_dictionaries'
    })


def create_type(request):
    if request.method == 'POST':
        form = TypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_dictionaries')
    else:
        form = TypeForm()

    return render(request, 'cash_flow_app/dictionary_form.html', {
        'form': form,
        'title': 'Добавить тип',
        'back_url': 'manage_dictionaries'
    })


def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_dictionaries')
    else:
        form = CategoryForm()

    return render(request, 'cash_flow_app/dictionary_form.html', {
        'form': form,
        'title': 'Добавить категорию',
        'back_url': 'manage_dictionaries'
    })


def create_subcategory(request):
    if request.method == 'POST':
        form = SubCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_dictionaries')
    else:
        form = SubCategoryForm()

    return render(request, 'cash_flow_app/dictionary_form.html', {
        'form': form,
        'title': 'Добавить подкатегорию',
        'back_url': 'manage_dictionaries'
    })


def edit_status(request, pk):
    status = get_object_or_404(Status, pk=pk)

    if request.method == 'POST':
        form = StatusForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            return redirect('manage_dictionaries')
    else:
        form = StatusForm(instance=status)

    return render(request, 'cash_flow_app/dictionary_form.html', {
        'form': form,
        'title': 'Редактировать статус',
        'back_url': 'manage_dictionaries'
    })


def edit_type(request, pk):
    type_obj = get_object_or_404(Type, pk=pk)

    if request.method == 'POST':
        form = TypeForm(request.POST, instance=type_obj)
        if form.is_valid():
            form.save()
            return redirect('manage_dictionaries')
    else:
        form = TypeForm(instance=type_obj)

    return render(request, 'cash_flow_app/dictionary_form.html', {
        'form': form,
        'title': 'Редактировать тип',
        'back_url': 'manage_dictionaries'
    })


def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('manage_dictionaries')
    else:
        form = CategoryForm(instance=category)

    return render(request, 'cash_flow_app/dictionary_form.html', {
        'form': form,
        'title': 'Редактировать категорию',
        'back_url': 'manage_dictionaries'
    })


def edit_subcategory(request, pk):
    subcategory = get_object_or_404(SubCategory, pk=pk)

    if request.method == 'POST':
        form = SubCategoryForm(request.POST, instance=subcategory)
        if form.is_valid():
            form.save()
            return redirect('manage_dictionaries')
    else:
        form = SubCategoryForm(instance=subcategory)

    return render(request, 'cash_flow_app/dictionary_form.html', {
        'form': form,
        'title': 'Редактировать подкатегорию',
        'back_url': 'manage_dictionaries'
    })


def delete_status(request, pk):
    status = get_object_or_404(Status, pk=pk)
    status.delete()
    return redirect('manage_dictionaries')


def delete_type(request, pk):
    type_obj = get_object_or_404(Type, pk=pk)
    type_obj.delete()
    return redirect('manage_dictionaries')


def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('manage_dictionaries')


def delete_subcategory(request, pk):
    subcategory = get_object_or_404(SubCategory, pk=pk)
    subcategory.delete()
    return redirect('manage_dictionaries')


def get_categories(request):
    type_id = request.GET.get('type_id')
    categories = Category.objects.filter(type_id=type_id)
    data = [{'id': cat.id, 'name': cat.name} for cat in categories]
    return JsonResponse(data, safe=False)


def get_subcategories(request):
    category_id = request.GET.get('category_id')
    subcategories = SubCategory.objects.filter(category_id=category_id)
    data = [{'id': sub.id, 'name': sub.name} for sub in subcategories]
    return JsonResponse(data, safe=False)