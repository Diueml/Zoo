# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: CraftBox
def sort_projects(projects, key='date'):
    if not projects: return []
    order = {'high': 0, 'medium': 1, 'low': 2}
    reverse = {key in ('name', 'budget')}.get(key) or False
    if key == 'date': reverse = True; key = lambda p: p.get('created_at', '')
    elif key == 'priority': key = lambda p: order.get(p.get('priority'), 3); reverse = False
    return sorted(projects, key=key, reverse=reverse)
