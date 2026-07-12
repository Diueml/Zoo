# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: CraftBox
def print_table(data, headers):
    """Выводит таблицу из списка словарей в консоль."""
    widths = [len(str(h)) for h in headers]
    for row in data:
        for i, v in enumerate(row.values()):
            if isinstance(v, str):
                widths[i] = max(widths[i], len(v))

    def fmt_row(values):
        return " | ".join(str(v).ljust(w) for v, w in zip(values, widths))

    print(f"{'─' * sum(widths + [2*(len(headers)+1)])}")
    print(fmt_row([str(h) for h in headers]))
    print(f"{'─' * sum(widths + [2*(len(headers)+1)])}")
    if data:
        print(fmt_row(data[0].values()))
        for row in data[1:]:
            print(fmt_row(row.values()))
