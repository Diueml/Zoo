# === Stage 32: Добавь журнал действий пользователя ===
# Project: CraftBox
class UserActionLog:
    def __init__(self):
        self.entries = []
    
    def log(self, action_type, description, details=None):
        entry = {
            'timestamp': datetime.now().isoformat(),
            'action_type': action_type,
            'description': description,
            'details': details or {}
        }
        self.entries.append(entry)
    
    def get_recent(self, count=10):
        return self.entries[-count:]

    def export_to_file(self, filename='user_log.json'):
        import json
        with open(filename, 'w') as f:
            json.dump(self.entries, f, indent=2, ensure_ascii=False)
