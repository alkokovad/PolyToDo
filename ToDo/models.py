from django.db import models
from django.contrib.auth.models import User


class Date(models.Model):
    date = models.DateTimeField()

    class Meta:
            verbose_name = 'Дата'
            verbose_name_plural = 'Даты'

    def __str__(self):
       return self.date


class ScheduleTemplate(models.Model):
    mn1 = models.CharField()
    tu1 = models.CharField()
    we1 = models.CharField()
    th1 = models.CharField()
    fr1 = models.CharField()
    st1 = models.CharField()
    su1 = models.CharField()
    mn2 = models.CharField()
    tu2 = models.CharField()
    we2 = models.CharField()
    th2 = models.CharField()
    fr2 = models.CharField()
    st2 = models.CharField()
    su2 = models.CharField()
    group = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
            verbose_name = 'Дата'
            verbose_name_plural = 'Даты'

    def __str__(self):
       return self.date