from django.db import models


class Reviews(models.Model):
    username = models.CharField('Имя пользователя', max_length=15)
    title = models.CharField('Тема(Заголовок)', max_length=30)
    rewiew = models.TextField('Отзыв')
    date = models.DateTimeField(
        'Дата публикации', auto_now=True, auto_now_add=False)

    def __str__(self):
        return(self.username)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
