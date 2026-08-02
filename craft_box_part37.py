# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: CraftBox
import unittest


class TestCraftBox(unittest.TestCase):
    def test_add_material(self):
        project = Project()
        mat = Material("wood", 50)
        project.add_material(mat)
        self.assertEqual(project.materials, [mat])

    def test_add_stage(self):
        project = Project()
        stage = Stage(1, "Design")
        project.add_stage(stage)
        self.assertEqual(project.stages, [stage])

    def test_add_idea(self):
        project = Project()
        idea = Idea("Make a clock", 100)
        project.add_idea(idea)
        self.assertEqual(project.ideas, [idea])

    def test_add_budget_item(self):
        project = Project()
        item = BudgetItem("lumber", 25.0)
        project.add_budget(item)
        self.assertAlmostEqual(project.total_cost, 25.0)


if __name__ == "__main__":
    unittest.main()
