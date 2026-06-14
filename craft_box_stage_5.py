# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: CraftBox
def delete_record(record_id, record_type):
    try:
        if not isinstance(record_id, int) or record_id <= 0:
            raise ValueError("ID должен быть положительным целым числом")
        
        db = get_db()
        key = f"{record_type}:{record_id}"
        data = db.get(key)
        
        if data is None:
            print(f"Запись {key} не найдена.")
            return False
        
        # Удаляем связанные данные (например, этапы проекта или идеи), если они хранятся отдельно
        related_keys = [f"{record_type}:{record_id}_stages", f"{record_type}:{record_id}_ideas"]
        for rel_key in related_keys:
            if db.get(rel_key):
                del db[rel_key]
        
        # Удаляем саму запись и её метаданные (если есть)
        metadata_key = f"metadata:{key}"
        if db.get(metadata_key):
            del db[metadata_key]
            
        del db[key]
        print(f"Запись {key} успешно удалена.")
        return True
        
    except Exception as e:
        print(f"Ошибка при удалении записи {record_type}:{record_id}: {e}")
        return False
