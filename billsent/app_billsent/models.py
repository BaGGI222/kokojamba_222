from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
from django.contrib.auth import get_user_model


User = get_user_model()


class Billsent(models.Model):
    title = models.CharField(verbose_name='Название', max_length=128)
    description = models.TextField('Описание')  
    price = models.DecimalField('Цена',max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Укажите, если возможен торг')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, color = 'red')
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)
    image = models.ImageField('изобржение', upload_to='billsent/')

    @admin.display(description = 'дата создания')
    def created_date(self):
        if self.create_at.date() == timezone.now().date():
            created_time = self.create_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_time
            )
        return self.create_at.strftime('%d.%m.%Y')
    
    @admin.display(description = 'изображение')
    def get_html_image(self):
            if self.image:
                return format_html(
                    '<img src = "{url}" style = "max-width: 80px; maax height: 80px;">', url = self.image.url
                )

def __str__(self):
    return f'Billsent(id={self.id}, title = {self.title}, price = {self.price})'


class Meta:
    db_table = 'billsent'
# Create your models here.
