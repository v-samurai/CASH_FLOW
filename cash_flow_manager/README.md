# Cash Flow Manager (Управление Денежными Потоками)

Система для учета и управления движением денежных средств (ДДС) с поддержкой категорий, подкатегорий и гибкой системой фильтрации.

---

## Возможности 📊

- Учет доходов и расходов  
- Гибкая система категорий и подкатегорий 🏷️  
- Расширенная фильтрация записей 🔍  
- Адаптивный интерфейс (Bootstrap 5) 📱  
- Динамическая загрузка данных (AJAX) 📈  
- Управление справочниками (статусы, типы, категории) 🗂️  
- SQLite база данных 💾  

---

## Технологический стек

- Backend: Django 4.2.7  
- Frontend: Bootstrap 5, JavaScript  
- Database: SQLite3  
- Язык: Python 3.11  

---

## Установка и запуск

### Предварительные требования

- Python 3.11+  
- pip  
- virtualenv (рекомендуется)  

### Шаги

1. **Клонирование репозитория**
git clone <your-repository-url>
cd cash_flow_manager

2. **Создание виртуального окружения**
python -m venv venv
source venv/bin/activate # Linux/Mac

или для Windows:
venv\Scripts\activate


3. **Установка зависимостей**
pip install -r requirements.txt


4. **Настройка базы данных**
python manage.py makemigrations
python manage.py migrate


5. **Загрузка начальных данных**
python manage.py load_initial_data


6. **Запуск сервера**
python manage.py runserver


Приложение будет доступно по адресу: [http://127.0.0.1:8000](http://127.0.0.1:8000/)

---

## Структура базы данных

- **CashFlowRecord** — записи о движении средств  
- **Status** — статусы операций (например: "Выполнено", "Ожидание")  
- **Type** — типы операций (например: "Доход", "Расход")  
- **Category** — категории операций  
- **SubCategory** — подкатегории операций  

---

## Использование

- **Главная страница** — просмотр всех записей в табличном виде  
- Фильтрация по дате, статусу, типу, категории  
- Пагинация (по 20 записей на странице)  
- Добавление записи с формой и валидацией данных  
- Динамическая загрузка категорий и подкатегорий  
- Поддержка комментариев к операциям  
- Управление справочниками: CRUD операции для статусов, типов, категорий и подкатегорий  
- Валидация уникальности записей  

---

## API Endpoints

- `GET /api/categories/?type_id=` — получение категорий по типу  
- `GET /api/subcategories/?category_id=` — получение подкатегорий по категории  

---

## Структура проекта
cash_flow_manager/
├── cash_flow_project/ # Настройки проекта
├── cash_flow_app/ # Основное приложение
│ ├── management/
│ │ └── commands/
│ │ └── load_initial_data.py
│ ├── migrations/ # Миграции базы данных
│ ├── templates/
│ │ └── cash_flow_app/ # Шаблоны
│ │ ├── base.html
│ │ ├── index.html
│ │ ├── record_form.html
│ │ ├── dictionaries.html
│ │ └── dictionary_form.html
│ ├── models.py # Модели данных
│ ├── views.py # Представления
│ ├── forms.py # Формы
│ └── urls.py # Маршруты
├── db.sqlite3 # База данных (создается автоматически)
└── manage.py # Управление Django


---

## Развертывание в production

Рекомендуется:

- Настроить PostgreSQL вместо SQLite  
- Установить `DEBUG = False`  
- Настроить статические файлы через `collectstatic`  
- Использовать WSGI сервер (Gunicorn + Nginx)  
- Настроить безопасные `SECRET_KEY` и другие параметры безопасности  

---

## Лицензия

MIT License — смотри файл LICENSE для деталей.

---

## Вклад в проект

- Форкните проект  
- Создайте feature ветку: `git checkout -b feature/amazing-feature`  
- Закоммитьте изменения: `git commit -m 'Add amazing feature'`  
- Запушьте в ветку: `git push origin feature/amazing-feature`  
- Откройте Pull Request  

---

## Поддержка

Если у вас есть вопросы или предложения, создайте issue в репозитории проекта.




