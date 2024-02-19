from .JobListing import JobListing
import random


# Software Engineer Job: Specialist
class SpecialistJob(JobListing):
    def __init__(self):
        super().__init__()
        self.potential_languages = ["c", "cpp", "c_sharp", "java", "javascript", "python"]
        self._calculate_specialist()

    def _calculate_specialist(self):
        chance = random.random()
        self._calculate_primary()
        self.skills["dsa"] = random.randint(14, 21)
        if chance >= 0.4:
            self.skills["sql"] = random.randint(4, 12)
        if chance >= 0.5:
            self._calculate_secondary()

    def _calculate_primary(self):
        chance = random.random()
        if chance >= 0.75:
            self.primary = "cpp"
        elif chance >= 0.55:
            self.primary = "java"
        elif chance >= 0.45:
            self.primary = "c_sharp"
        elif chance >= 0.25:
            self.primary = "c"
        elif chance >= 0.15:
            self.primary = "javascript"
        else:
            self.primary = "python"

        self.skills[self.primary] = random.randint(22, 30)
        self.potential_languages.remove(self.primary)

    def _calculate_secondary(self):
        self.secondary = random.choice(self.potential_languages)
        self.potential_languages.remove(self.secondary)
        self.skills[self.secondary] = random.randint(4, 12)
