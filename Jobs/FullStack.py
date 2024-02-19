from .JobListing import JobListing
import random


# Web Development Job: Full Stack
class FullStackJob(JobListing):
    def __init__(self):
        super().__init__()
        self._calculate_full_stack()

    def _calculate_full_stack(self):
        self._calculate_primary()
        chance = random.random()
        if self.primary != "javascript":
            self.secondary = "javascript"
            self.skills["javascript"] = random.randint(7, 18)
        self.skills["html"] = random.randint(10, 18)
        self.skills["css"] = random.randint(7, 15)
        if chance >= 0.5:
            self.skills["sql"] = random.randint(4, 12)
        if chance >= 0.3:
            self.skills["dsa"] = random.randint(3, 12)

    def _calculate_primary(self):
        chance = random.random()
        if chance >= 0.8:
            self.primary = "python"
        elif chance >= 0.55:
            self.primary = "php"
        elif chance >= 0.2:
            self.primary = "c_sharp"
        else:
            self.primary = "javascript"

        # sets the average skill level for primary language (range)
        self.skills[self.primary] = random.randint(13, 21)
