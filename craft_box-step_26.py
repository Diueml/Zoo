# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: CraftBox
def run_quick_demo():
    """Быстрый набор демо-команд для ручного тестирования CraftBox."""
    print("=== CraftBox Quick Demo ===")
    
    # 1. Инициализация
    box = ProjectManager()
    box.initialize()
    print(f"✅ CraftBox запущен.\n")
    
    # 2. Создание проекта
    project = box.create_project(
        id="demo-001", name="Мой первый проект", budget=5000, deadline="2024-12-31"
    )
    print(f"📁 Проект создан: {project.name} (ID: {project.id})")
    
    # 3. Добавление этапов
    phase = box.add_phase(project.id, name="Исследование", start_date="2024-01-01", duration_days=7)
    print(f"📋 Этап добавлен: {phase.name}")
    
    # 4. Добавление материалов
    materials = [
        {"name": "Бумага A4", "quantity": 10, "price": 50},
        {"name": "Карандаши", "quantity": 2, "price": 300},
        {"name": "Клей PVA", "quantity": 1, "price": 80},
    ]
    for m in materials:
        box.add_material(project.id, name=m["name"], quantity=m["quantity"], price=m["price"])
    
    print(f"📦 Добавлено {len(materials)} материалов")
    
    # 5. Добавление идей
    ideas = [
        {"title": "Концепция А", "description": "Классический стиль с деревянными элементами"},
        {"title": "Концепция Б", "description": "Минимализм с акцентом на натуральные цвета"},
    ]
    for idea in ideas:
        box.add_idea(project.id, title=idea["title"], description=idea["description"])
    
    print(f"💡 Добавлено {len(ideas)} идей")
    
    # 6. Просмотр проекта
    project_info = box.get_project(project.id)
    print(f"\n📊 Итоговый бюджет: {project_info['total_material_cost']}")
    print(f"   Этапов: {len(project_info['phases'])}")
    print(f"   Идеи: {len(project_info['ideas'])}")
    
    # 7. Обновление статуса проекта
    box.update_project_status(project.id, "in_progress")
    print(f"\n🔄 Статус обновлён: в процессе")

run_quick_demo()
