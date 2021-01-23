import sys
while True:
    _str = sys.stdin.readline().strip()
    if len(_str) >= 1:
        print(_str)
    else:
        break
'''
while True:
    try:
        print(input())
    except EOFError:
        break
'''