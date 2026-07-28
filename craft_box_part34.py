# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: CraftBox
TEMPLATE_REGISTRY = {}

def register_template(name, fields):
    TEMPLATE_REGISTRY[name] = fields

def create_from_template(template_name):
    if template_name not in TEMPLATE_REGISTRY:
        raise ValueError(f"Unknown template: {template_name}")
    return {field: "" for field in TEMPLATE_REGISTRY[template_name]}

register_template("project", ["name", "description", "status"])
register_template("idea", ["title", "tags", "priority"])
