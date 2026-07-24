# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: CraftBox
def switch_profile():
    """Переключение активного пользовательского профиля."""
    profiles = load_profiles()
    if not profiles:
        print("Нет доступных профилей.")
        return
    profile_name = input(f"Выберите профиль ({', '.join(profiles)}): ").strip() or list(profiles)[0]
    while profile_name not in profiles:
        print("Неверное имя профиля. Попробуйте снова.")
        profile_name = input("Выберите профиль: ").strip()
    active_profile = find_active_user()
    if active_profile and active_profile['name'] != profile_name:
        confirm = input(f"Сменить профиль с '{active_profile['name']}' на '{profile_name}'? (y/n): ").lower()
        if confirm != 'y':
            print("Отмена.")
            return
    save_active_user(profile_name)
    print(f"Активный профиль: {profile_name}")
