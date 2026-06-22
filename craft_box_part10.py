# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: CraftBox
def export_to_json():
    import json
    from datetime import datetime
    data = {
        "projects": projects,
        "ideas": ideas,
        "materials": materials,
        "stages": stages,
        "budgets": budgets,
        "timestamp": datetime.now().isoformat()
    }
    return json.dumps(data, indent=2, ensure_ascii=False)
