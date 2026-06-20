# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: CraftBox
import json, sys

def load_initial_data(json_string: str) -> dict:
    try:
        data = json.loads(json_string)
        if not isinstance(data, dict):
            raise ValueError("JSON должен содержать объект")
        
        # Валидация структуры данных
        required_keys = ["projects", "materials", "ideas", "budget"]
        missing_keys = [k for k in required_keys if k not in data]
        if missing_keys:
            raise KeyError(f"Отсутствуют ключи: {', '.join(missing_keys)}")
        
        # Валидация типов данных для каждого раздела
        if not isinstance(data["projects"], list):
            raise TypeError("projects должен быть списком")
        for i, proj in enumerate(data["projects"]):
            if not isinstance(proj.get("id"), (int, str)):
                raise ValueError(f"Проект {i}: id должен быть строкой или числом")
            
        if not isinstance(data["materials"], list):
            raise TypeError("materials должен быть списком")
        
        if not isinstance(data["ideas"], list):
            raise TypeError("ideas должен быть списком")
            
        # Валидация бюджета (простая)
        budget = data.get("budget", {})
        if "total" in budget and not isinstance(budget["total"], (int, float)):
            raise ValueError("Бюджет total должен быть числом")
        
        return data
    
    except json.JSONDecodeError as e:
        print(f"[CraftBox] Ошибка парсинга JSON: {e}", file=sys.stderr)
        sys.exit(1)

# Пример использования (раскомментируйте для теста):
if __name__ == "__main__":
    sample_json = '''
{
  "projects": [{"id": 1, "title": "Веб-сайт", "status": "planning"}],
  "materials": [{"type": "html", "content": "<h1>Hello</h1>"}],
  "ideas": ["Идея 1", "Идея 2"],
  "budget": {"total": 5000, "currency": "USD"}
}'''

    # Загрузка данных из строки JSON
    craftbox_data = load_initial_data(sample_json)
    
    print(f"[CraftBox] Успешно загружено {len(craftbox_data['projects'])} проектов.")
