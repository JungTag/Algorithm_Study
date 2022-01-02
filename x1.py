def solution(info, query):
    answer = []
    applicants = dict()

    languages = ['cpp', 'java', 'python']
    jobs = ['backend', 'frontend']
    careers = ['junior', 'senior']
    foods = ['chicken', 'pizza']

    init_dict(languages, jobs, careers, foods, applicants)

    for i in info:
        language, job, career, food, score = i.split()
        applicants[language][job][career][food].append(int(score))

    for q in query:
        language, job, career, food_and_score = q.split(' and ')
        food, score = food_and_score.split()
        score = int(score)
        cur_dict = dict()

        if language == '-':
            for l in languages:
                cur_dict.update(applicants[l])
        else:
            cur_dict = applicants[language]

    print(applicants)
    return answer


def init_dict(languages, jobs, careers, foods, applicants):

    for language in languages:
        add_dict(language, applicants)
        for job in jobs:
            add_dict(job, applicants[language])
            for career in careers:
                add_dict(career, applicants[language][job])
                for food in foods:
                    add_dict(food, applicants[language][job][career])
                    applicants[language][job][career][food] = []


def add_dict(key, cur_dict):
    if key not in cur_dict:
        cur_dict[key] = dict()


def dig(key, parent_dict, target_list, applicants):
    cur_dict = dict()

    for k in parent_dict:
        if key == '-':
            for t in target_list:
                cur_dict.update(applicants[t]) # 안됨!!
        else:
            cur_dict.update(parent_dict[key])

    return cur_dict

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])