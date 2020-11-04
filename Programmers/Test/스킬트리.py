def solution(skill, skill_trees):
    answer = 0
    for candidate_skill in skill_trees:
        for i in range(len(skill)):
            char = skill[i]; front = skill[:i]; tail = skill[i+1:]; esc = False
            if char in candidate_skill:
                obj = candidate_skill.index(char)
                for k in range(obj-1,-1,-1):
                    if candidate_skill[k] in tail:
                        esc = True
                        break
                for l in range(obj+1,len(candidate_skill)):
                    if candidate_skill[l] in front:
                        esc = True
                        break
            else:
                for x in range(i+1, len(skill)):
                    if skill[x] in candidate_skill:
                        esc = True
                        break
            if esc == True: break
        if esc == False:
            answer += 1
    return answer