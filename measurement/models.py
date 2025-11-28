from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")

    def __str__(self):
        return f"{self.name} (ID: {self.id})"


class Measurement(models.Model):
    sensor = models.ForeignKey(
        Sensor,
        on_delete=models.CASCADE,
        related_name='measurements',
        verbose_name="Датчик"
    )
    temperature = models.FloatField(verbose_name="Температура, °C")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время измерения")
    image = models.ImageField(upload_to='measurements/', blank=True, null=True, verbose_name="Фото")

    def __str__(self):
        return f"{self.sensor.name}: {self.temperature}°C at {self.created_at}"