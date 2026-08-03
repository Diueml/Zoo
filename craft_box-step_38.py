# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: CraftBox
def test_edge_cases():
    """Compact edge-case tests for CraftBox."""
    from craftbox import App
    
    app = App()
    
    # 1) Negative material quantity
    mat = Material("wood", -5, 0.5)
    assert mat.quantity == 0 and mat.cost == 0, "Negative qty/cost rejected"
    
    # 2) Zero duration stage
    stage = Stage("Plan", "", 0)
    assert not stage.completed, "Zero-duration stage must be incomplete"
    
    # 3) Budget exceeded when adding item
    app.add_stage(Stage("Build", "assemble box", 10))
    app.add_material(Material("glue", 5, 2.0))
    app.add_idea(Idea("use recycled wood"))
    app.set_budget(Budget(30))
    
    try:
        app.add_stage(Stage("Paint", "paint box", 10))
    except BudgetExceeded:
        pass  # expected
    
    # 4) Empty title stage
    stage = Stage("", "details", 5)
    assert not stage.completed, "Empty-title stage must be incomplete"
    
    # 5) Duplicate material in budget
    app.add_material(Material("screws", 10, 0.3))
    try:
        app.add_material(Material("screws", 20, 0.4))
    except MaterialExists:
        pass
    
    print("All edge-case tests passed.")

test_edge_cases()
