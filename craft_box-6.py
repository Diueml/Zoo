# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: CraftBox
def filter_projects(criteria=None):
    if not criteria: return projects_list
    filtered = []
    for p in projects_list:
        match_status = criteria.get('status') is None or p['status'] == criteria['status']
        match_category = criteria.get('category') is None or p['category'] == criteria['category']
        match_tags = not criteria.get('tags') or any(t in p['tags'] for t in criteria['tags'])
        if match_status and match_category and match_tags: filtered.append(p)
    return filtered
