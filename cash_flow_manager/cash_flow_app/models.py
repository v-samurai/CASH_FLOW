from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название")

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название")

    class Meta:
        verbose_name = "Тип операции"
        verbose_name_plural = "Типы операций"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название")
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name="Тип операции")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"
        unique_together = ('name', 'category')

    def __str__(self):
        return f"{self.category} - {self.name}"


class CashFlowRecord(models.Model):
    date = models.DateField(verbose_name="Дата операции")
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name="Статус")
    type = models.ForeignKey(Type, on_delete=models.PROTECT, verbose_name="Тип операции")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Категория")
    subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT, verbose_name="Подкатегория")
    amount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Сумма")
    comment = models.TextField(blank=True, null=True, verbose_name="Комментарий")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Запись о движении средств"
        verbose_name_plural = "Записи о движении средств"
        ordering = ['-date']

    def __str__(self):
        return f"{self.date} - {self.amount} руб. - {self.category}"