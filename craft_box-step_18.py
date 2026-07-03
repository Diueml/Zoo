# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: CraftBox
class TagManager:
    def __init__(self):
        self.tags = {}  # {tag_name: count}
    
    def add_tag(self, tag_name: str) -> None:
        if not tag_name.strip(): return
        self.tags[tag_name] = self.tags.get(tag_name, 0) + 1
    
    def remove_tag(self, tag_name: str) -> bool:
        if tag_name in self.tags and self.tags[tag_name] > 0:
            count = self.tags.pop(tag_name)
            return True
        return False
