from itertools import combinations

def solution(relation):
    COL_LEN = len(relation[0])
    ROW_LEN = len(relation)

    answer = 0
    columns = []
    duplicated_column_indexes = []
    candidate_keys = []

    # init
    for i in range(COL_LEN):
        new_column = []
        for j in range(ROW_LEN):
            new_column.append(relation[j][i])
        columns.append(new_column)

    # check
    for i, column in enumerate(columns):
        if len(set(column)) == ROW_LEN:
            answer += 1
        else:
            duplicated_column_indexes.append(i)

    for n in range(2, len(duplicated_column_indexes)+1):
        for combi in combinations(duplicated_column_indexes, n):
            combi_set = set(combi)

            if not is_minimal(combi_set, candidate_keys):
                continue

            if is_candidate_key(combi, columns, ROW_LEN):
                answer += 1
                candidate_keys.append(combi_set)

    return answer


def is_minimal(combi_set, candidate_keys):
    for candidate_key in candidate_keys:
        if combi_set & candidate_key == candidate_key:
            return False
    return True


def is_candidate_key(indexes, columns, ROW_LEN):
    checked_key = set()

    for row in range(ROW_LEN):
        new_column = ""
        for index in indexes:
            new_column += columns[index][row]
        checked_key.add(new_column)
    
    if len(checked_key) == ROW_LEN:
        return True
    else:
        return False


print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))