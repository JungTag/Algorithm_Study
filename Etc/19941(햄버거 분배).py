import sys

n, k = map(int, sys.stdin.readline().split())
p = sys.stdin.readline().strip()

visited = set()
person = []

for i, x in enumerate(p):
    if x == "P":
        person.append(i)

for i in range(len(person)):
    idx = person[i]
    for j in range(idx-k, idx+k+1):
        if 0<=j<n and p[j]=="H" and j not in visited:
            visited.add(j)
            break

print(len(visited))