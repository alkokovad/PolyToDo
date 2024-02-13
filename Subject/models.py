from django.db import models
from ToDo.models import Date


class Subject(models.Model):
    name = models.CharField(max_length=9, verbose_name='Название предмета в 9 символов')

    class Meta:
            verbose_name = 'Предмет'
            verbose_name_plural = 'Предметы'

    def __str__(self):
       return self.name


class Homework(models.Model):
    subject = models.ForeignKey(Date, on_delete=models.CASCADE)
    date = models.DateTimeField()
    description = models.CharField(max_length=600, verbose_name='ДЗ')
    documents = models.CharField()

    class Meta:
            verbose_name = 'Домашка'
            verbose_name_plural = 'Домашки'

    def __str__(self):
       return f'{self.date} - {self.subject}'
