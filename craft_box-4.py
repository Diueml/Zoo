# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: CraftBox
def edit_record(record_id, updates):
    if not isinstance(updates, dict) or len(updates) == 0:
        raise ValueError("Обновления должны быть словарем с хотя бы одним полем")
    
    for key in list(records.keys()):
        try:
            current = records[key]
            if isinstance(current, dict):
                new_record = {**current}
                for k, v in updates.items():
                    if k in new_record and not callable(v) and not (isinstance(v, type(new_record[k])) or isinstance(v, str)):
                        raise TypeError(f"Тип поля '{k}' не совпадает")
                    new_record[k] = v
            else:
                continue
        except Exception as e:
            print(f"Ошибка редактирования записи {key}: {e}")
            break
    else:
        records[record_id] = updates
