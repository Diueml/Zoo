# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: CraftBox
def show_record(record):
    """Compact one-line summary with details."""
    if not record:
        return "No records available."
    r = record[0]
    title = r.get("title", "?")
    status = r.get("status", "?")
    budget_total = sum(v for v in (r.get("budget_items", [])) if isinstance(v, dict) and v.get("total"))
    ideas_count = len(r.get("ideas", []))
    materials = ", ".join(m["name"] for m in r.get("materials", [])[:3]) + ("..." if len(r.get("materials", [])) > 3 else "")
    return f"Project: {title} | Status: {status} | Budget used: ${budget_total:.0f}/{r.get('total_budget', 'N/A')} | Ideas: {ideas_count} | Materials: {materials}"
