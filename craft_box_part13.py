# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: CraftBox
def search_projects(query, fields=None):
    if not query: return []
    q = query.lower()
    if fields is None: fields = ['name', 'idea', 'materials', 'notes']
    results = [p for p in projects if any(q in str(getattr(p, f, '')).lower() for f in fields)]
    return sorted(results, key=lambda x: (getattr(x, 'priority', 0), getattr(x, 'created_at', '')), reverse=True)
