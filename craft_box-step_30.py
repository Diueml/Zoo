# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: CraftBox
def manage_profiles():
    profiles = {
        "admin": {"role": "admin", "name": "Администратор"},
        "editor": {"role": "editor", "name": "Редактор"},
        "viewer": {"role": "viewer", "name": "Наблюдатель"}
    }

    def add_profile(name, role):
        if name in profiles:
            return False
        profiles[name] = {"role": role, "name": name}
        return True

    def remove_profile(name):
        if name not in profiles or profiles[name]["role"] == "admin":
            return False
        del profiles[name]
        return True

    def get_profile(name):
        return profiles.get(name)

    def list_profiles():
        return profiles.copy()

    def set_active_profile(name):
        if name not in profiles:
            return False
        for p in profiles.values():
            p["active"] = (p["name"] == name and p["role"] != "admin")
        return True

    return add_profile, remove_profile, get_profile, list_profiles, set_active_profile
