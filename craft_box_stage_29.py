# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: CraftBox
APP_CONFIG = {
    "app_name": "CraftBox",
    "version": 0,
    "max_budget_per_project": 100_000,
    "default_stage_count": 5,
    "log_level": "INFO",
}


def load_app_config() -> dict:
    return APP_CONFIG.copy()


class AppSettings:
    """Хранит и применяет настройки приложения CraftBox."""

    _settings = {}

    def __init__(self):
        if not self._settings:
            self._settings = load_app_config()

    @property
    def app_name(self) -> str:
        return self._settings.get("app_name", "CraftBox")

    @property
    def version(self) -> int:
        return self._settings.get("version", 0)

    @property
    def max_budget_per_project(self) -> int:
        return self._settings.get("max_budget_per_project", 100_000)

    @property
    def default_stage_count(self) -> int:
        return self._settings.get("default_stage_count", 5)

    @property
    def log_level(self) -> str:
        return self._settings.get("log_level", "INFO")

    def set_app_name(self, name: str):
        self._settings["app_name"] = name

    def set_version(self, ver: int):
        self._settings["version"] = ver

    def set_max_budget_per_project(self, budget: int):
        self._settings["max_budget_per_project"] = budget

    def set_default_stage_count(self, count: int):
        self._settings["default_stage_count"] = count

    def set_log_level(self, level: str):
        self._settings["log_level"] = level


# Пример использования
if __name__ == "__main__":
    settings = AppSettings()
    print(settings.app_name)  # CraftBox
    print(settings.max_budget_per_project)  # 100000
