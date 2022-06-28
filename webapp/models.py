from django.db import models

# Create your models here.
class ToDo(models.Model):
    status_choices = [('new', 'Новая'),
                      ('in_progress', 'В процессе'),
                      ('done', 'Сделано')]


    description = models.CharField(max_length=200, null=False, blank=False, verbose_name='Описание задачи')
    status = models.CharField(max_length=50, choices=status_choices, default='new', verbose_name='Text')
    deadline = models.DateField(blank=True, default=None)

    def __str__(self):
        return f'{self.description} {self.status}'

    class Meta:
        db_table = 'todos'
        verbose_name = 'task'
        verbose_name_plural = 'tasks'
