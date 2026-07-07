# === Stage 20: Добавь восстановление записей из архива ===
# Project: CraftBox
def restore_from_archive(archive_path, project_db):
    """Restore project records from a JSON archive file."""
    import json
    try:
        with open(archive_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Ошибка при загрузке архива: {e}")
        return 0

    records = data.get('projects', []) if isinstance(data, dict) else [data]
    restored_count = 0
    for rec in records:
        pid = rec.get('_id') or rec.get('project_id') or len(project_db.projects) + 1000
        project_db.projects.append({
            '_id': pid,
            'name': rec.get('name', f'Восстановленный проект {pid}'),
            'description': rec.get('description', ''),
            'budget': rec.get('budget', 0),
            'materials': rec.get('materials', []),
            'stages': rec.get('stages', []),
            'ideas': rec.get('ideas', []),
            'created_at': rec.get('created_at', None)
        })
        restored_count += 1

    print(f"Восстановлено {restored_count} записей из архива.")
    return restored_count
