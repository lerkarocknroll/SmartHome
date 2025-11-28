from django.urls import path
from . import views

urlpatterns = [
    path('sensors/', views.create_sensor, name='create_sensor'),
    path('sensors/<int:pk>/', views.update_sensor, name='update_sensor'),
    path('measurements/', views.add_measurement, name='add_measurement'),
    path('sensors/<int:pk>/detail/', views.sensor_detail, name='sensor_detail'),
]