from .JobListing import JobListing
import random


# Web Development Job: Back End
class BackEndJob(JobListing):
    def __init__(self):
        super().__init__()
        self.potential_languages = ["python", "php", "c_sharp", "javascript"]
        self._calculate_back_end()

    def _calculate_back_end(self):
        self._calculate_primary()
        self._calculate_secondary()
        chance = random.random()

        # 50% chance of HTML / CSS req
        if chance >= 0.5:
            self.skills["html"] = random.randint(5,12)
            self.skills["css"] = random.randint(4, 11)

        # 80% chance of DSA req
        if chance >= 0.2:
            self.skills["dsa"] = random.randint(10, 20)

        # Add Javascript req if not already included
        if "javascript" in self.potential_languages:
            self.skills["javascript"] = random.randint(5, 12)

        # Add SQL req
        self.skills["sql"] = random.randint(3, 16)

    def _calculate_primary(self):
        chance = random.random()
        if chance >= 0.8:
            self.primary = "python"
            self.potential_languages.remove("python")
        elif chance >= 0.55:
            self.primary = "php"
            self.potential_languages.remove("php")
        elif chance >= 0.2:
            self.primary = "c_sharp"
            self.potential_languages.remove("c_sharp")
        else:
            self.primary = "javascript"
            self.potential_languages.remove("javascript")

        # sets the average skill level for primary language (range)
        self.skills[self.primary] = random.randint(15, 22)

    def _calculate_secondary(self):
        secondary = random.choice(self.potential_languages)
        self.secondary = secondary
        self.potential_languages.remove(secondary)

        # sets the average skill level for secondary language (range)
        self.skills[self.secondary] = random.randint(13, 21)
