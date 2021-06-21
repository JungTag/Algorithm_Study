import re

def solution(S, C):
    result = []
    addresses = []
    name_dict = {}
    email = f"@{C.lower()}.com"
    full_names = [re.sub('[^a-zA-Z\s]', '', s).strip().lower() for s in S.split(',')]

    for full_name in full_names:
        splited_name = full_name.split()
        len_of_name = len(splited_name)
        name = ""
        for i, each_name in enumerate(splited_name):
            if i == len_of_name-1:
                name += each_name[:8]
            else:
                name += each_name[0]
        if name in name_dict:
            name_dict[name] += 1
            name += str(name_dict[name])
        else:
            name_dict[name] = 1
        addresses.append(f"<{name}{email}>")

    for address, full_name in zip(addresses, [re.sub('[^a-zA-z\s-]', '', s).strip() for s in S.split(',')]):
        result.append(f"{full_name} {address}")
    
    return ", ".join(result)

