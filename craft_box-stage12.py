# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: CraftBox
import json, os

def load_projects_from_file(file_path: str) -> list[dict]:
    if not os.path.exists(file_path):
        print(f"Файл {file_path} не найден.")
        return []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        elif isinstance(data, dict) and "projects" in data:
            return data["projects"]
        else:
            print("Неверный формат JSON файла.")
            return []
    except json.JSONDecodeError as e:
        print(f"Ошибка чтения JSON: {e}")
        return []
