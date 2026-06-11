# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: CraftBox
class ProjectManager:
    def __init__(self):
        self.projects = {}
        self.materials = []
        self.ideas = []
        self.budget_log = []

    def add_project(self, name, budget=0):
        if name in self.projects:
            print(f"Проект '{name}' уже существует.")
            return False
        self.projects[name] = {"budget": budget, "stages": [], "notes": ""}
        print(f"Проект '{name}' создан с бюджетом {budget}.")
        return True

    def add_stage(self, project_name, stage_name, deadline=None):
        if project_name not in self.projects:
            print(f"Проект '{project_name}' не найден.")
            return False
        self.projects[project_name]["stages"].append({
            "name": stage_name,
            "deadline": deadline
        })
        print(f"Этап '{stage_name}' добавлен к проекту '{project_name}'.")
        return True

    def add_material(self, name, quantity, cost):
        self.materials.append({"name": name, "quantity": quantity, "cost": cost})
        print(f"Материал '{name}' добавлен.")
        return True

    def add_idea(self, title, description):
        self.ideas.append({"title": title, "description": description})
        print(f"Идея '{title}' сохранена.")
        return True

    def log_budget_change(self, project_name, amount, reason):
        if project_name not in self.projects:
            print(f"Проект '{project_name}' не найден для записи бюджета.")
            return False
        current_budget = self.projects[project_name]["budget"]
        new_budget = current_budget + amount
        self.projects[project_name]["budget"] = new_budget
        self.budget_log.append({
            "project": project_name,
            "amount": amount,
            "reason": reason,
            "new_total": new_budget
        })
        print(f"Бюджет проекта '{project_name}' изменен на {new_budget} ({reason}).")
        return True

    def get_project_summary(self, name):
        if name not in self.projects:
            return None
        p = self.projects[name]
        total_material_cost = sum(m["cost"] for m in self.materials)
        return {
            "name": name,
            "current_budget": p["budget"],
            "stages_count": len(p["stages"]),
            "total_material_cost": total_material_cost,
            "notes": p["notes"]
        }

    def list_projects(self):
        return list(self.projects.keys())
