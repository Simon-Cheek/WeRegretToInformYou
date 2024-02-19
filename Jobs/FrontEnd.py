from .JobListing import JobListing
import random


# Web Development Job: Front End
class FrontEndJob(JobListing):
    def __init__(self):
        super().__init__()
        self._calculate_front_end()

    def _calculate_front_end(self):
        self._calculate_primary()
        chance = random.random()
        self.skills["html"] = random.randint(13, 25)
        self.skills["css"] = random.randint(12, 22)
        self.secondary = "javascript"
        self.skills["javascript"] = random.randint(8, 25)
        if chance >= 0.85:
            self.skills["dsa"] = random.randint(2, 8)

    def _calculate_primary(self):
        chance = random.random()
        if chance >= 0.6:
            self.primary = "python"
        elif chance >= 0.25:
            self.primary = "php"
        else:
            self.primary = "c_sharp"

        # sets the average skill level for primary language (range)
        self.skills[self.primary] = random.randint(5, 12)
