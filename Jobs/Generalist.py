from .JobListing import JobListing
import random


# Software Engineer Job: Generalist
class GeneralistJob(JobListing):
    def __init__(self):
        super().__init__()
        self.potential_languages = ["c", "cpp", "c_sharp", "java", "javascript", "python"]
        self._calculate_specialist()

    def _calculate_specialist(self):
        chance = random.random()
        self._calculate_primary()
        self._calculate_secondary()
        self.skills["dsa"] = random.randint(5, 16)
        if chance >= 0.2:
            self.skills["sql"] = random.randint(8, 12)
        if chance >= 0.75:
            hidden = random.choice(self.potential_languages)
            self.skills[hidden] = random.randint(1, 8)
            self.potential_languages.remove(hidden)

    def _calculate_primary(self):
        chance = random.random()
        if chance >= 0.8:
            self.primary = "cpp"
        elif chance >= 0.65:
            self.primary = "java"
        elif chance >= 0.45:
            self.primary = "c_sharp"
        elif chance >= 0.3:
            self.primary = "c"
        elif chance >= 0.2:
            self.primary = "javascript"
        else:
            self.primary = "python"

        self.skills[self.primary] = random.randint(10, 22)
        self.potential_languages.remove(self.primary)

    def _calculate_secondary(self):
        self.secondary = random.choice(self.potential_languages)
        self.potential_languages.remove(self.secondary)
        self.skills[self.secondary] = random.randint(9, 18)
