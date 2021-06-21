import datetime

def solution(S):
    result = []
    months = {
        "Jan": 1,
        "Feb": 2,
        "Mar": 3,
        "Apr": 4,
        "May": 5,
        "Jun": 6,
        "Jul": 7,
        "Aug": 8,
        "Sep": 9,
        "Oct": 10,
        "Nov": 11,
        "Dec": 12
    }

    for raw in S.split("\n"):
        owner = raw[:6].strip()
        perm = raw[7:11].strip()
        date = raw[11:23].strip()
        size = int(raw[23:33].strip())
        if "x" in perm and owner == "admin" and size < 14 * 2**20:
            splited_date = date.split()
            y = int(splited_date[2])
            m = int(months[splited_date[1]])
            d = int(splited_date[0])
            criteria = datetime.date(y, m, d)
            result.append([date, criteria])
            
    if not result:
        return "NO FILES"
    
    return sorted(result, key = lambda r: r[1])[0][0]