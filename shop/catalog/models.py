
from django.db import models
from django.urls import reverse


from django.db.models.deletion import CASCADE

from django.db.models.fields.related import ForeignKey



 



class Byke(models.Model):
    title = models.CharField(max_length= 100, verbose_name = 'Название велосипеда')
    description = models.TextField(verbose_name= 'Описание')
    material_ram = models.CharField(max_length= 100, verbose_name = 'Материал рамы' )
    updated_at = models.DateTimeField(auto_now=True)
    transmission = models.IntegerField(verbose_name = 'Количество передач')
    diameter_wheel = models.IntegerField(verbose_name = 'Диаметр колес' )
    photo = models.ImageField(upload_to='photos/%Y/%m/', blank=True)
    price = models.CharField(max_length= 100, verbose_name = 'Цена (BYN)', default="Договорнаяя")
    type_of_ram = models.BooleanField(blank=True, verbose_name = 'Складная рама')
    slug = models.SlugField(max_length= 100, verbose_name= 'Слаг', db_index=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True,)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("item_page_byke", kwargs={"slug_id": self.slug})
    


    class Meta:
        verbose_name = 'Велосипед'
        verbose_name_plural = 'Велосипеды'
        ordering = ['-updated_at', 'title']



class Scooter(models.Model):
    title = models.CharField(max_length= 100, verbose_name = 'Название самоката', null=True)
    description = models.TextField(verbose_name= 'Описание', null=True)
    material_ram = models.CharField(max_length= 100, verbose_name = 'Материал рамы', null=True )
    updated_at = models.DateTimeField(auto_now=True, null=True)
    weight = models.CharField(max_length= 100, verbose_name = 'Вес', null=True)
    bearings = models.CharField(max_length= 100, verbose_name = 'Подшибники', null=True )
    photo = models.ImageField(upload_to='photos/%Y/%m/', null=True)
    price = models.CharField(max_length= 100, verbose_name = 'Цена (BYN)', default="Договорнаяя", null=True)
    type_of_ram = models.BooleanField(blank=True, verbose_name = 'Складная рама', null=True)
    slug = models.SlugField(max_length= 100, verbose_name= 'Слаг', null=True, db_index=True)
    category = models.ForeignKey('Category',on_delete=models.PROTECT, null=True,)
    


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "item_page_scooter",
             kwargs={
            "slug_pk": self.slug
        })


    class Meta:
        verbose_name = 'Самокат'
        verbose_name_plural = 'Самокаты'
        ordering = ['-updated_at', 'title']


class Category(models.Model):
    title = models.CharField(max_length=255,db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length= 100, verbose_name= 'Слаг', null=True, db_index=True)

    def __str__(self):
        return self.title


    # def get_absolute_url(self):
    #     return reverse("item_page_byke", kwargs={"slug_category": self.slug})


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Img(models.Model):
    photo = models.ImageField(upload_to='photos/%Y/%m/', null=True)


