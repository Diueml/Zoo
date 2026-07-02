# === Stage 17: Добавь группировку записей по категориям ===
# Project: CraftBox
def group_by_category(records):
    groups = {}
    for record in records:
        cat = record.get('category', 'Uncategorized')
        if cat not in groups:
            groups[cat] = []
        groups[cat].append(record)
    return dict(sorted(groups.items()))
