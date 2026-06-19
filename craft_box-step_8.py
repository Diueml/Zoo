# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: CraftBox
def run_cli():
    print("=== CraftBox CLI ===")
    while True:
        cmd = input("\nКоманда (проект/материалы/этапы/идеи/бюджет/выход): ").strip().lower()
        if not cmd: continue
        parts = cmd.split(maxsplit=1)
        action, arg = parts[0], parts[1] if len(parts) > 1 else ""
        
        projects = get_projects(); materials = get_materials(); stages = get_stages(); ideas = get_ideas(); budget = get_budget()
        
        if action == "проект":
            print(f"Проекты: {', '.join(p['name'] for p in projects)}")
            if arg:
                proj = next((p for p in projects if p['name'].lower() == arg), None)
                if proj:
                    print(proj); continue
                else:
                    new_proj = input("Новое имя проекта: ")
                    add_project(new_proj, materials.copy(), stages.copy())
        elif action == "материалы":
            print(f"Материалы для {arg or 'всех'}:\n{materials}")
        elif action == "этапы":
            if arg and projects:
                proj = next((p for p in projects if p['name'].lower() == arg), None)
                if proj: print(f"Этапы проекта '{proj['name']}': {stages.get(proj['id'], [])}")
        elif action == "идеи":
            print(f"Идеи:\n{ideas}")
        elif action == "бюджет":
            total = sum(p.get('budget', 0) for p in projects); spent = sum(m.get('cost', 0) for m in materials if m['project_id'])
            print(f"Бюджет: {total} (израсходовано: {spent})")
        elif action == "выход": break
        else: print("Неизвестная команда.")
