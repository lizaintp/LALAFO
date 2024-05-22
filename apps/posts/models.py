from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Загаловок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    price = models.PositiveIntegerField(
        verbose_name='Цена'
    )
    image = models.ImageField(
        upload_to='postsimage/',
        verbose_name='Изображение товара'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

