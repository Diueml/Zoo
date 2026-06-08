# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: CraftBox
import json
from pathlib import Path

# Конфигурация и точка входа
APP_NAME = "CraftBox"
DATA_FILE = Path(__file__).parent / "data.json"

def load_data():
    if not DATA_FILE.exists():
        return {
            "projects": [],
            "materials": [],
            "ideas": [],
            "budget": {"total": 0, "spent": 0}
        }
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# Демонстрационные данные для инициализации
def init_demo():
    data = load_data()
    if not data["projects"]:
        demo_project = {
            "id": 1,
            "name": "Мой первый проект",
            "status": "planning",
            "budget_limit": 10000,
            "spent": 0,
            "stages": [
                {"name": "Идея", "done": True},
                {"name": "Подготовка", "done": False}
            ]
        }
        data["projects"].append(demo_project)
        save_data(data)
        print(f"Демо-данные для {APP_NAME} созданы.")

if __name__ == "__main__":
    init_demo()
