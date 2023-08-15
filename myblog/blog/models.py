from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    # Дані про пости
    title = models.CharField('Заголовок запису', max_length=100)
    description = models.TextField('Текст запису')
    author = models.CharField("Ім'я автора", max_length=100)
    date = models.DateField('Дата публікації')
    img = models.ImageField('Іллюстрація', upload_to='image/%Y')

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = "Запис"
        verbose_name_plural = "Запиcи"


class Comments(models.Model):
    name = models.ForeignKey(User, verbose_name="Автор коментаря", on_delete=models.CASCADE, blank=True, null=True)
    text_comments = models.TextField('Текст комментаря', max_length=2000)
    post = models.ForeignKey(Post, verbose_name="Публікація", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.post}'

    class Meta:
        verbose_name = "Коментар"
        verbose_name_plural = "Коментарі"
