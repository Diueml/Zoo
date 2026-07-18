# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: CraftBox
import json, os

def reset_demo_data():
    """Сбрасывает все демо-данные в исходное состояние."""
    default_data = {
        "materials": [
            {"id": 1, "name": "Бумага A4", "quantity": 500, "unit": "шт"},
            {"id": 2, "name": "Краска акриловая", "quantity": 24, "unit": "мл"},
            {"id": 3, "name": "Карандаш графитный", "quantity": 10, "unit": "шт"},
        ],
        "stages": [
            {"id": 1, "title": "Концепция", "description": "Оформить идею и набросать эскиз", "order": 1},
            {"id": 2, "title": "Прототипирование", "description": "Создать прототип из доступных материалов", "order": 2},
            {"id": 3, "title": "Тестирование", "description": "Проверить работоспособность и качество результата", "order": 3},
        ],
        "ideas": [
            {"id": 1, "title": "Праздничный шар", "description": "Создать декоративный шар из бумаги"},
            {"id": 2, "title": "Арт-карта", "description": "Нарисовать карту мира акриловыми красками"},
        ],
        "budget": {
            "total": 1000.0,
            "spent": 350.0,
            "currency": "USD"
        }
    }
    with open("craftbox_data.json", "w") as f:
        json.dump(default_data, f, indent=2)
    print(f"[CraftBox] Демо-данные сброшены. Файл craftbox_data.json обновлён.")

def clear_state():
    """Полностью удаляет файл данных CraftBox."""
    if os.path.exists("craftbox_data.json"):
        os.remove("craftbox_data.json")
    print("[CraftBox] Состояние полностью очищено. Файл craftbox_data.json удалён.")
