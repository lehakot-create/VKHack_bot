from django.db import models


class Employee(models.Model):
    surname = models.CharField(max_length=128, verbose_name='Фамилия')
    name = models.CharField(max_length=128, verbose_name='Имя')
    surname2 = models.CharField(max_length=128,
                                verbose_name='Отчество',
                                null=True)
    birthday = models.DateField(verbose_name='День рождения')
    job_title = models.ForeignKey('JobTitle',
                                  on_delete=models.DO_NOTHING,
                                  verbose_name='Должность')
    date_time_contract = models.DateField(
        verbose_name='Дата подписания трудового контракта'
        )
    department = models.ForeignKey('Department',
                                   on_delete=models.DO_NOTHING,
                                   verbose_name='Отдел')
    mentor = models.ForeignKey('Mentor',
                               on_delete=models.DO_NOTHING,
                               verbose_name='Наставник')
    uuid = models.CharField(max_length=64, null=True)


class JobTitle(models.Model):
    name = models.CharField(max_length=32, verbose_name='Должность')

    def __str__(self):
        return f'{self.name}'


class Department(models.Model):
    name = models.CharField(max_length=128, verbose_name='Отдел')

    def __str__(self):
        return f'{self.name}'


class Mentor(models.Model):
    name = models.CharField(max_length=128, verbose_name='Наставник')

    def __str__(self):
        return f'{self.name}'
