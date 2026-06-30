# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: CraftBox
def generate_monthly_stats(data, start_date, end_date):
    from datetime import date, timedelta
    stats = {}
    current = start_date
    while current <= end_date:
        month_key = f"{current.year}-{current.month}"
        if month_key not in stats:
            stats[month_key] = {'ideas': 0, 'materials_added': 0, 'budget_spent': 0.0}
        
        for item in data:
            item_date = date.fromisoformat(item['date'])
            if item_date.year == current.year and item_date.month == current.month:
                if 'idea' in item: stats[month_key]['ideas'] += 1
                if 'material' in item: stats[month_key]['materials_added'] += 1
                if 'budget_change' in item: stats[month_key]['budget_spent'] += float(item['budget_change'])
        
        current = current.replace(day=1) + timedelta(days=32)
    return stats
