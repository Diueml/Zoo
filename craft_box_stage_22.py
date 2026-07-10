# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: CraftBox
def check_overdue_reminders(self):
        today = datetime.date.today()
        overdue = [r for r in self.reminders if r['date'] < today]
        for reminder in overdue:
            print(f"  ⚠️  Просрочено: {reminder['text']} (было {reminder['date'].isoformat()}).")
