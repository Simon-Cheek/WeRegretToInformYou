from BackEnd import BackEndJob
from Generalist import GeneralistJob
from Specialist import SpecialistJob
from FrontEnd import FrontEndJob
from FullStack import FullStackJob
import random


def generate_jobs():

    jobs_list = []

    # generate 5 jobs and add to final array
    for i in range(5):
        chance = random.random()
        if chance >= 0.8:
            new_job = BackEndJob()
        elif chance >= 0.6:
            new_job = GeneralistJob
        elif chance >= 0.4:
            new_job = SpecialistJob
        elif chance >= 0.2:
            new_job = FrontEndJob
        else:
            new_job = FullStackJob
        jobs_list.append(new_job)

    return jobs_list

