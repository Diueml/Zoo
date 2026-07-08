# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: CraftBox
def add_reminders(projects):
    reminders = {}
    for project in projects:
        if 'reminders' not in project:
            project['reminders'] = []
        for reminder in project.get('reminders', []):
            task = reminder['task']
            date = reminder['date']
            key = (project['name'], task)
            reminders[key] = date

    while True:
        print("\n=== Напоминания CraftBox ===")
        if not reminders:
            print("Нет активных напоминаний.")
        else:
            for i, ((pname, task), date) in enumerate(reminders.items(), 1):
                print(f"{i}. [{pname}] {task} — {date}")

        action = input("\nДействие (1=добавить, 2=показать, 3=завершить): ").strip()
        if action == '1':
            pname = input("Название проекта: ")
            task = input("Задача напоминания: ")
            date_input = input("Дата (YYYY-MM-DD или 'сегодня'): ")
            from datetime import date, timedelta
            today = date.today()
            if date_input == 'сегодня':
                target_date = today
            else:
                try:
                    target_date = date.fromisoformat(date_input)
                except ValueError:
                    print("Неверный формат даты.")
                    continue

            project_name = None
            for p in projects:
                if p['name'] == pname:
                    project_name = p
                    break
            if not project_name:
                print("Проект не найден.")
                continue

            reminder = {
                'task': task,
                'date': target_date.isoformat(),
                'done': False
            }
            if 'reminders' in project_name and reminder['date'] <= today:
                reminder['done'] = True
                reminders[(pname, task)] = target_date

            project_name.setdefault('reminders', []).append(reminder)
            print(f"Напоминание добавлено: {task} ({target_date})")

        elif action == '2':
            if not reminders:
                print("Нет активных напоминаний.")
            else:
                for i, ((pname, task), date) in enumerate(reminders.items(), 1):
                    print(f"{i}. [{pname}] {task} — {date}")

        elif action == '3':
            done_count = sum(1 for _, info in reminders.items() if info['done'])
            if done_count:
                print(f"Завершено {done_count} напоминаний.")
            else:
                print("Нет завершенных напоминаний.")

        elif action == 'q' or action == 'quit':
            break
