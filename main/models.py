from django.db import models


class SiteModel(models.Model):
    """Модель поста с сайтом из портфолио"""
    name = models.CharField(max_length=150, verbose_name="Имя сайта")
    desc = models.TextField(verbose_name='Описание')
    link_to_site = models.URLField(verbose_name="Ссылка на сайт")
    link_to_rep = models.URLField(verbose_name='Ссылка на репозиторий')
    login_on_pythonanywhere = models.CharField(max_length=150, verbose_name='Логин')
    image = models.ImageField(verbose_name='Картинка',
                              upload_to=f"images/")
    

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Сайт'
        verbose_name_plural = 'Сайты'

