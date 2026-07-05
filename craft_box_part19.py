# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: CraftBox
def archive_projects(projects, cutoff_date=None):
    if not projects: return []
    from datetime import datetime
    today = datetime.now().date()
    cutoff = cutoff_date or (today.replace(day=1) - timedelta(days=30)).replace(day=1)
    archived = [p for p in projects if p.get('status') == 'completed' and p['end_date'] <= cutoff]
    active = [p for p in projects if p not in archived]
    return {'archived': archived, 'active': active}
