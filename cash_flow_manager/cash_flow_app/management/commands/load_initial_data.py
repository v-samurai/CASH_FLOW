from django.core.management.base import BaseCommand
from cash_flow_app.models import Status, Type, Category, SubCategory


class Command(BaseCommand):
    help = 'Загружает начальные данные для приложения управления ДДС'

    def handle(self, *args, **options):
        self.stdout.write('Загрузка начальных данных...')

        # Создаем статусы
        statuses = ['Бизнес', 'Личное', 'Налог']
        for status_name in statuses:
            Status.objects.get_or_create(name=status_name)
            self.stdout.write(f'Создан статус: {status_name}')

        # Создаем типы операций
        types = ['Пополнение', 'Списание']
        for type_name in types:
            Type.objects.get_or_create(name=type_name)
            self.stdout.write(f'Создан тип: {type_name}')

        # Получаем тип "Списание" для категорий
        spending_type = Type.objects.get(name='Списание')

        # Создаем категории и подкатегории
        categories_data = {
            'Инфраструктура': ['VPS', 'Proxy'],
            'Маркетинг': ['Farpost', 'Avito']
        }

        for category_name, subcategories in categories_data.items():
            category, created = Category.objects.get_or_create(
                name=category_name,
                defaults={'type': spending_type}
            )
            self.stdout.write(f'Создана категория: {category_name}')

            for subcategory_name in subcategories:
                SubCategory.objects.get_or_create(
                    name=subcategory_name,
                    category=category
                )
                self.stdout.write(f'Создана подкатегория: {subcategory_name} для категории {category_name}')

        self.stdout.write(self.style.SUCCESS('Начальные данные успешно загружены!'))