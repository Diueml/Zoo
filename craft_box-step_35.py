# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: CraftBox
def get_next_action(project):
    """Рекомендует следующее действие на основе текущего состояния проекта."""
    if not project:
        return "Создайте новый проект."
    
    status = project.get("status", "")
    ideas = project.get("ideas", [])
    steps = project.get("steps", [])
    budget = project.get("budget", 0)

    if not ideas and not steps and budget == 0:
        return "Начните с идеи — добавьте хотя бы одну в список идей проекта."

    if not steps and status != "completed":
        return "Определите следующие шаги проекта и добавьте их в список этапов."

    if steps and not project.get("timeline", None):
        return "Составьте таймлайн для запланированных шагов, указав даты начала и окончания."

    if budget == 0:
        return "Укажите бюджет проекта — это поможет отслеживать финансовые ограничения."

    return "Проект выглядит полным. Рассмотрите возможность его завершения или добавьте новые идеи."
