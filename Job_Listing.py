import random

class JobListing:
    def __init__(self):
        self.primary = ""
        self.secondary = ""
        self.skills = {
            "html": 0,
            "css": 0,
            "javascript": 0,
            "c_sharp": 0,
            "c": 0,
            "python": 0,
            "sql": 0,
            "cpp": 0,
            "java": 0,
            "php": 0,
            "dsa": 0
        }


# Web Development Job: Front End
class FrontEndJob(JobListing):
    def __init__(self):
        super().__init__()
        self.calculate_front_end()

    def calculate_front_end(self):
        pass


# Web Development Job: Back End
class BackEndJob(JobListing):
    def __init__(self):
        super().__init__()
        self.calculate_back_end()

    def calculate_back_end(self):
        pass


# Web Development Job: Full Stack
class FullStackJob(JobListing):
    def __init__(self):
        super().__init__()
        self.calculate_full_stack()

    def calculate_full_stack(self):
        pass


# Software Engineer Job: Specialist
class SpecialistJob(JobListing):
    def __init__(self):
        super().__init__()
        self.calculate_specialist()

    def calculate_specialist(self):
        pass


# Software Engineer Job: Generalist
class GeneralistJob(JobListing):
    def __init__(self):
        super().__init__()
        self.calculate_generalist()

    def calculate_generalist(self):
        pass





