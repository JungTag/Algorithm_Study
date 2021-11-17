# https://programmers.co.kr/learn/courses/30/lessons/17686

def solution(files):
    formatted_files = []

    for i, file in enumerate(files):
        is_number_start = False
        number_start_index = -1
        number_end_index = -1

        for j, char in enumerate(file):
            if is_number_start and not char.isdigit():
                break
            if not is_number_start and char.isdigit():
                is_number_start = True
                number_start_index = number_end_index = j
            elif is_number_start and char.isdigit():
                number_end_index = j

        formatted_files.append(
            [file[:number_start_index].lower(),
            int(file[number_start_index:number_end_index+1]),
            i]) # [HEAD, NUMBER, INDEX]

    formatted_files.sort(key = lambda x: (x[0], x[1], x[2]))

    answer = list(map(lambda x: files[x[2]], formatted_files))

    return answer


print(solution(["img0.png", "img00000.png", "img0", "img0 asdf", "img0 "]))
# print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
# a = ["-B", "-A"]
# print(sorted(a))

# a = "-B adfa ESD"
# print(a.lower())

# a = "00012"
# print(int(a))