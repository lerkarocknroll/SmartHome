from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Sensor, Measurement
from .serializers import (
    SensorSerializer,
    SensorDetailSerializer,
    MeasurementSerializer
)


@api_view(['POST'])
def create_sensor(request):
    serializer = SensorSerializer(data=request.data)
    if serializer.is_valid():
        sensor = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def update_sensor(request, pk):
    try:
        sensor = Sensor.objects.get(pk=pk)
    except Sensor.DoesNotExist:
        return Response({'error': 'Sensor not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = SensorSerializer(sensor, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_measurement(request):
    serializer = MeasurementSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_sensors(request):
    sensors = Sensor.objects.all()
    serializer = SensorSerializer(sensors, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def sensor_detail(request, pk):
    try:
        sensor = Sensor.objects.prefetch_related('measurements').get(pk=pk)
    except Sensor.DoesNotExist:
        return Response({'error': 'Sensor not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = SensorDetailSerializer(sensor)
    return Response(serializer.data)