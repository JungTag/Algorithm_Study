from collections import defaultdict
from fractions import Fraction

def solution(character, monsters):
    answer = ''
    monster_dict = defaultdict(list)
    player_hp, player_sp, player_dp = map(int, character.split())

    for i, monster in enumerate(monsters):
        monster_name = monster.split()[0]
        monster_ep, monster_hp, monster_sp, monster_dp = map(int, monster.split()[1:])

        dmg_player_to_monster = player_sp - monster_dp
        dmg_monster_to_player = monster_sp - player_dp
        player_rest_hp, monster_rest_hp = player_hp, monster_hp

        time = 0

        if dmg_monster_to_player < player_hp and dmg_player_to_monster <= 0:
            continue

        while monster_rest_hp > 0 and player_rest_hp > 0:
            time += 1
            player_rest_hp = player_hp
            monster_rest_hp -= dmg_player_to_monster
            player_rest_hp -= dmg_monster_to_player

        if monster_rest_hp <= 0:
            monster_dict[monster_name] = [Fraction(monster_ep, time), monster_ep, i]
    
    answer = monsters[sorted(monster_dict.values(), key=lambda x: (-x[0], -x[1], x[2]))[0][2]].split()[0]

    return answer

print(solution("10 5 2",["Knight 3 10 10 3","Wizard 5 10 15 1","Beginner 1 1 15 1"]))