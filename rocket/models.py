from django.db import models
from django.contrib.auth.models import User


# python manage.py makemigrations
# python manage.py migrate

class LaunchVehicle(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    short_description = models.TextField(blank=True, null=True, verbose_name="Краткое описание")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    gto_playload = models.IntegerField(verbose_name="Полезная нагрузка (кг)")
    imagerocket = models.ImageField(verbose_name="Изображение",blank=True, null=True,
                                upload_to="rockets/")
    is_active = models.BooleanField(verbose_name = "Активно", default=True)

    class Meta:
        verbose_name = "Ракета-носитель"
        verbose_name_plural = "Ракеты-носители"

    def __str__(self):
        return self.name
    
# class SpacePort(models.Model):
#     name = models.CharField(max_length=100, verbose_name="Название космодрома")
#     descriptionSP = models.TextField(blank=True, null=True, verbose_name="Описание")
#     location = models.IntegerField(verbose_name="Широта космодрома")

#     class Meta:
#         verbose_name = "Космодром"
#         verbose_name_plural = "Космодромы"

#     def __str__(self):
#         return self.name
    

class Order(models.Model):
    class OrderStatus(models.TextChoices):
        DRAFT = "Черновик"
        DELETED = "Удален"
        FORMED = "В расчете"
        COMPLETED = "Расчет завершен"
        REJECTED = "Ошибка в расчете"

    status = models.CharField(
        max_length=25,
        choices=OrderStatus.choices,
        default=OrderStatus.DRAFT,
    )

    creation_datetime = models.DateTimeField(auto_now_add=True)
    formation_datetime = models.DateTimeField(blank=True, null=True)
    completion_datetime = models.DateTimeField(blank=True, null=True)
    client = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='created_orders')
    #manager = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='managed_orders', blank=True, null=True)

    def __str__(self):
        return f"Заказ № {self.id}"


class CalculationRequest(models.Model):
     
    #user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    order = models.ForeignKey(Order,null=True,on_delete=models.DO_NOTHING, verbose_name="Пользователь")
    rocket = models.ForeignKey(LaunchVehicle, on_delete=models.DO_NOTHING, verbose_name="Ракета")
    port_name = models.CharField(max_length=100, verbose_name="Порт",blank=True, null=True)
    comment = models.TextField(blank=True, null=True, verbose_name="Комментарий")
    location = models.IntegerField(verbose_name="Широта космодрома",blank=True, null=True)
    result = models.IntegerField(verbose_name="Результат вычислений")
    
    # port = models.ForeignKey(SpacePort, on_delete=models.CASCADE, verbose_name="Порт")

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return f"{self.user} - {self.rocket} - {self.port}"



     



