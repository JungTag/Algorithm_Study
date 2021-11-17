from collections import defaultdict

def solution(table, languages, preference):
    answer = ''
    table = [table[i].split() for i in range(5)] 
    job_score_dict = defaultdict(int)
    language_preference_dict = dict(zip(languages, preference))

    for i in range(5):
        job = table[i][0]
        for j in range(1, 6):
            language = table[i][j]
            if language in languages:
                job_score_dict[job] += (6 - j) * language_preference_dict[language]

    max_score_jobs = [job for job, score in job_score_dict.items() if max(job_score_dict.values()) == score]
    answer = sorted(max_score_jobs)[0]

    return answer
