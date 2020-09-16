'''
1. zip 사용하면 두 개의 리스트를 편하게 합칠 수 있음
2. 탑2 장르만 뽑는 실수를 저지름
'''
def solution(genres, plays):
    answer = []
    song_dict = {}
    for i in range(len(genres)):
        if genres[i] in song_dict.keys():
            song_dict[genres[i]].append([plays[i], i])
            song_dict[genres[i]][0] += plays[i] # for 1번 조건(총합 기록)
        else:
            song_dict[genres[i]] = [plays[i], [plays[i], i]]
            
    song_dict_items = list(song_dict.items())
    song_dict_items.sort(key = lambda x : -x[1][0]) # 1번 조건
    for genre, play_list in song_dict_items:
        play_list.remove(play_list[0])
        play_list.sort(key = lambda x : (-x[0], x[1])) # 2번 조건 + 3번 조건
    for i in range(len(song_dict_items)):
        play_list = song_dict_items[i][1]
        if len(play_list) >= 2:
            answer.append(play_list[0][1])
            answer.append(play_list[1][1])
        else:
            answer.append(play_list[0][1])
    return answer

# Test Case

# genres = ["classic", "pop", "classic", "pop", "classic", "classic"]
# plays = [400, 600, 150, 2500, 500, 500]
# genres =['c','a','b','a','a','b','b','b','b','c','c','c','d']
# plays =[1,500,9, 600, 501, 800,500,300,2,2,1,2,100000]
# solution(genres, plays)

# solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 800, 800, 2500])
# solution(["classic", "pop", "classic", "classic", "pop", "jpop"], [500, 600, 150, 800, 2500, 3000])
# solution(["classic", "pop"], [500, 600])
# solution(["classic"], [500])
