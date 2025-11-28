```markdown
# 🏠 Smart Home API

REST API для системы умного дома: регистрация температурных датчиков и сбор измерений (температура, время, опционально — фото).

Реализовано на **Django REST Framework (DRF)**. Полностью покрывает CRUD-логику для датчиков и измерений.

---

## 📦 Функционал

- ✅ Создание, обновление и просмотр датчиков  
- ✅ Добавление измерений температуры  
- ✅ Поддержка прикрепления фото к измерению (опционально)  
- ✅ Вложенные сериализаторы: в ответе по датчику — список всех измерений  
- ✅ Автоматическая установка времени измерения (`created_at`)

---

## 🛠️ Технологии

- Python 3.9+
- Django 4.2+
- Django REST Framework
- PostgreSQL (рекомендуется)
- `Pillow` (для работы с изображениями)

---

## 📁 Структура моделей

```python
Sensor
├── id: int
├── name: str
└── description: str (опционально)

Measurement
├── sensor: ForeignKey → Sensor
├── temperature: float
├── created_at: datetime (автозаполнение)
└── image: ImageField (опционально)
```

---

## 📡 API Эндпоинты

| Метод | URL | Описание |
|-------|-----|----------|
| `POST` | `/api/sensors/` | Создать датчик (`name`, `description`) |
| `PATCH` | `/api/sensors/<id>/` | Обновить датчик (частичное обновление) |
| `POST` | `/api/measurements/` | Добавить измерение (`sensor`, `temperature`, [`image`]) |
| `GET` | `/api/sensors/list/` | Получить список датчиков (кратко) |
| `GET` | `/api/sensors/<id>/detail/` | Получить датчик с полной информацией и измерениями |

### Пример ответа (датчик + измерения):

```json
{
  "id": 1,
  "name": "ESP32",
  "description": "На балконе",
  "measurements": [
    {
      "temperature": 22.4,
      "created_at": "2025-11-28T14:30:00.123456Z",
      "image": "http://127.0.0.1:8000/media/measurements/balcony_abc123.jpg"
    },
    {
      "temperature": 22.7,
      "created_at": "2025-11-28T14:45:00.987654Z",
      "image": null
    }
  ]
}
```

> 📸 Поле `image` может быть `null`, если фото не прикреплено.

---

## 🚀 Установка и запуск

1. **Клонировать репозиторий**
   ```bash
   git clone https://github.com/your-username/smart-home-api.git
   cd smart-home-api
   ```

2. **Создать и активировать виртуальное окружение**
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\Scripts\activate      # Windows
   ```

3. **Установить зависимости**
   ```bash
   pip install -r requirements.txt
   ```

4. **Настроить базу данных**
   - Создайте БД в PostgreSQL (например, `smart_home`)
   - Обновите `DATABASES` в `smart_home/settings.py`

5. **Применить миграции**
   ```bash
   python manage.py migrate
   ```

6. **(Опционально) Создать суперпользователя**
   ```bash
   python manage.py createsuperuser
   ```

7. **Запустить сервер**
   ```bash
   python manage.py runserver
   ```

---

## 📁 Медиафайлы

Для загрузки фото:
- Убедитесь, что в `settings.py` заданы:
  ```python
  MEDIA_URL = '/media/'
  MEDIA_ROOT = BASE_DIR / 'media'
  ```
- В корневом `urls.py` подключена раздача медиа в `DEBUG`-режиме:
  ```python
  if settings.DEBUG:
      urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  ```

---
