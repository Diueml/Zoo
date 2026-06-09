# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: CraftBox
class ValidationError(Exception):
    pass

def validate_input(data: dict) -> dict:
    errors = []
    if not isinstance(data, dict):
        raise ValidationError("Ввод должен быть словарём")
    for key in ["name", "budget"]:
        if key not in data or not isinstance(data[key], str):
            errors.append(f"Отсутствует или неверен ключ '{key}'")
    if "name" in data and len(data["name"].strip()) < 2:
        errors.append("Имя проекта должно быть не менее 2 символов")
    if "budget" in data:
        try:
            budget = float(data["budget"])
            if budget < 0:
                errors.append("Бюджет не может быть отрицательным")
        except ValueError:
            errors.append("Неверный формат бюджета")
    return {"errors": errors, "data": data}
