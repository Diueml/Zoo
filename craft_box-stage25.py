# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: CraftBox
def parse_date(raw):
    """Парсит дату в формате 'YYYY-MM-DD' или 'DD.MM.YYYY'.
    Возвращает datetime.date, либо строку с описанием ошибки."""
    if not raw:
        return "Ошибка: дата не задана."

    formats = ["%Y-%m-%d", "%d.%m.%Y"]
    s = raw.strip()
    for fmt in formats:
        try:
            d = datetime.strptime(s, fmt)
            return d.date().isoformat()
        except ValueError:
            continue
    return f"Ошибка: не распознана дата '{raw}'. Используйте формат YYYY-MM-DD или DD.MM.YYYY."
