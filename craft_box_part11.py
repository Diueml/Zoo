# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: CraftBox
import json, os

def save_data(data: dict, file_path: str = "craftbox.json") -> None:
    """Сохраняет данные проекта в JSON файл с обработкой ошибок."""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"[OK] Данные сохранены в {file_path}")
    except (json.JSONDecodeError, IOError) as e:
        print(f"[ERROR] Не удалось сохранить данные: {e}")

def load_data(file_path: str = "craftbox.json") -> dict | None:
    """Загружает данные из JSON файла или возвращает пустой словарь при ошибке."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        print("[WARN] Файл данных не найден или поврежден. Создаётся новый.")
        return {}
