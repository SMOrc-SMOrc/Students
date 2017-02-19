from django.db import models


class Students(models.Model):
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    middle_name = models.CharField('Отчество', max_length=50)
    record_book = models.ForeignKey('RecordBook', blank=True, null=True)

    def __str__(self):
        return self.first_name


class RecordBook(models.Model):
    number = models.CharField('Номер книжки', unique=True, max_length=7)
    student = models.ForeignKey(Students)

