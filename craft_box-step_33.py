# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: CraftBox
import json, os

def undo_last_entry(data_path="craftbox.json"):
    if not os.path.exists(data_path):
        return None
    with open(data_path, "r") as f:
        data = json.load(f)
    keys = list(data.keys())
    last_key = keys[-1]
    del data[last_key]
    with open(data_path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    return data.get(last_key)

if __name__ == "__main__":
    undone = undo_last_entry()
    if undone is not None:
        print(f"Отменено действие с ключом: {list(undone.keys())[0] if isinstance(undone, dict) else 'скаляр'}")
