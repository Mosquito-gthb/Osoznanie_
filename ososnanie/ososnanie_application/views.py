import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from models import get_message # Импортируем твою функцию. Обычно её кладут в файл logic.py или models.py

# @csrf_exempt нужно, чтобы отключить защиту CSRF для API.
# Для учебного проекта это нормально. В реальном проекте используют другие методы.
@csrf_exempt 
def submit_answers_view(request):
    # 1. Проверяем, что это POST-запрос
    if request.method == 'POST':
        try:
            # 2. Извлекаем JSON-пакет из тела запроса
            data = json.loads(request.body)
            
            # 3. Вызываем функцию для извлечения данных (как ты и хотел)
            # Это делает код чище, хотя можно было и напрямую data.get() использовать.
            answers = data.get('numbers')
            gender = data.get('gender')

            # 4. Проверяем, что данные пришли
            if not answers or gender is None:
                return JsonResponse({"status": "error", "message": "Пакет данных неполный. Нужны 'numbers' и 'gender'."}, status=400)

            # 5. Вызываем твою главную функцию логики
            # Она возвращает словарь: {"total_score": total, "interpretation": message}
            result_data = get_message(answers, gender) 

            # 6. Формируем финальный ответ для фронтенда
            response = {
                "status": "success",
                **result_data  # Здесь мы распаковываем твой словарь в основной ответ
                # Теперь ответ выглядит так: {"status": "success", "total_score": ..., "interpretation": ...}
            }

            return JsonResponse(response)

        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Некорректный формат JSON."}, status=400)

    # Если метод запроса не POST
    return JsonResponse({"status": "error", "message": "Метод не поддерживается."}, status=405)
