# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: CraftBox
def generate_summary():
    if not projects: return "Нет проектов для сводки."
    total_budget = sum(p.get('budget', 0) for p in projects.values())
    spent = sum(sum(stage.get('spent', 0) for stage in p['stages'].values()) for p in projects.values())
    remaining = total_budget - spent
    active_count = len([p for p in projects.values() if any(s.get('status') == 'in_progress' for s in p['stages'].values())])
    print(f"Сводка CraftBox: {len(projects)} проектов, активные: {active_count}")
    print(f"Бюджет: {total_budget:.2f}, затрачено: {spent:.2f}, осталось: {remaining:.2f}")
