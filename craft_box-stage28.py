# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: CraftBox
def project_metrics(projects):
    if not projects:
        return {"total": 0, "active": 0, "completed": 0}
    active = sum(p["status"] == "active" for p in projects)
    completed = sum(p["status"] == "completed" for p in projects)
    total_budget = sum(sum(step.get("budget", 0) for step in p.get("stages", [])) for p in projects if any(step.get("budget", 0) > 0 for step in p.get("stages", [])))
    return {"total": len(projects), "active": active, "completed": completed, "total_budget_spent": total_budget}
