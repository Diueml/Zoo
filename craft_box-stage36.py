# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: CraftBox
def check_and_repair_data():
    """Check data integrity and repair simple issues in-place."""
    issues = []
    
    if not isinstance(materials, dict) or len(materials) == 0:
        materials = {}
        issues.append("materials dictionary is empty or invalid")
    
    if not isinstance(stages, list):
        stages = []
        issues.append("stages is not a list")
    
    for i, stage in enumerate(stages):
        if not isinstance(stage, dict) or 'name' not in stage:
            if isinstance(stage, str):
                stages[i] = {'name': stage}
            else:
                stages[i] = {}
                issues.append(f"stage at index {i} is invalid")
    
    for i, idea in enumerate(ideas):
        if not isinstance(idea, dict) or 'title' not in idea:
            if isinstance(idea, str):
                ideas[i] = {'title': idea}
            else:
                ideas[i] = {}
                issues.append(f"idea at index {i} is invalid")
    
    if not isinstance(budget, (int, float)):
        budget = 0.0
        issues.append("budget is not a number")
    
    repair_count = len(issues)
    return repair_count > 0

if __name__ == "__main__":
    print("CraftBox Manager v1.0")
    if check_and_repair_data():
        print("Data repaired successfully!")
