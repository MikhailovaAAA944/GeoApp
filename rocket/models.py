from django.db import models
from django.contrib.auth.models import User

# python manage.py makemigrations
# python manage.py migrate

class LaunchVehicle(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    short_description = models.TextField(blank=True, null=True, verbose_name="Краткое описание")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    gto_playload = models.IntegerField(verbose_name="Полезная нагрузка (кг)")
    imagerocket = models.ImageField(verbose_name="Изображение",upload_to="rockets/",blank=True, null=True)

    class Meta:
        verbose_name = "Ракета-носитель"
        verbose_name_plural = "Ракеты-носители"

    def __str__(self):
        return self.name
    
class SpacePort(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название космодрома")
    descriptionSP = models.TextField(blank=True, null=True, verbose_name="Описание")
    location = models.IntegerField(verbose_name="Широта космодрома")

    class Meta:
        verbose_name = "Космодром"
        verbose_name_plural = "Космодромы"

    def __str__(self):
        return self.name
    

class CalculationRequest(models.Model):
     
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    rocket = models.ForeignKey(LaunchVehicle, on_delete=models.CASCADE, verbose_name="Ракета")
    port = models.ForeignKey(SpacePort, on_delete=models.CASCADE, verbose_name="Порт")
    comment = models.TextField(blank=True, null=True, verbose_name="Комментарий")
    result = models.IntegerField(verbose_name="Результат вычислений")

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return f"{self.user} - {self.rocket} - {self.port}"



     



