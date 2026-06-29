# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: CraftBox
def calculate_weekly_statistics(projects):
    from collections import defaultdict
    weekly_stats = defaultdict(lambda: {'count': 0, 'total_budget': 0})
    for proj in projects:
        if not hasattr(proj, 'start_date') or not hasattr(proj, 'end_date'): continue
        try:
            start = datetime.strptime(str(proj.start_date), '%Y-%m-%d').date()
            end = datetime.strptime(str(proj.end_date), '%Y-%m-%d').date()
            current_week_start = (start - timedelta(days=start.weekday())).isoformat()
            weekly_stats[current_week_start]['count'] += 1
            weekly_stats[current_week_start]['total_budget'] += proj.budget
        except ValueError: pass
    return dict(sorted(weekly_stats.items()))
