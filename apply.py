import random


def apply(job, player):

    # Job Application Algorithm

    tested_skills = ["html", "css", "javascript", "php", "c", "cpp", "c_sharp", "python", "sql", "java", "dsa"]
    player_total = 0
    job_total = 0
    skills_lacking = 0

    for test in tested_skills:
        if job.skills[test] > 0:

            # increment each total that exists on the listing
            player_total += player.skills[test]
            job_total += job.skills[test]

        # player can't be more than 4 behind any skill
        if job.skills[test] > (player.skills[test] + 4):
            return False
        if job.skills[test] > player.skills[test]:
            skills_lacking += 1

    # player can't be behind at all on the primary skill
    if job.skills[job.primary] > player.skills[job.primary]:
        return False

    # 85% chance of failure if behind on dsa
    chance = random.random()
    if (job.skills["dsa"] > player.skills["dsa"]) and (chance >= 0.15):
        return False

    # rejection values depending on how many skills are lacking
    chance = random.random()
    if skills_lacking > 3:
        return False
    elif skills_lacking > 2 and chance >= 0.1:
        return False
    elif skills_lacking > 1 and chance >= 0.4:
        return False
    elif skills_lacking == 1 and chance >= 0.75:
        return False

    # finally, win conditions
    chance = random.random()
    if job_total > player_total and chance >= 0.2:
        return False
    elif job_total == player_total and chance >= 0.3:
        return False
    elif (player_total - job_total) < 5 and chance >= 0.4:
        return False
    elif (player_total - job_total) >= 5 and chance >= 0.5:
        return False

    return True
