from django.db import models

class Products(models.Model):
    name = models.CharField("Название товара", max_length=50)
    description = models.TextField("Описание товара")
    price = models.IntegerField("Цена товара")
    image_source = models.ImageField("Картинка товара", blank=False, upload_to="images/")

    def __str__(self):
        return self.name