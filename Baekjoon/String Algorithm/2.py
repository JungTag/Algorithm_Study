import sys

class Trie:
    head = {}

    def add(self, foods):
        cur = self.head
        
        for food in foods:
            if food not in cur:
                cur[food] = {}
            cur = cur[food]
    
    
    def travel(self):
        cur = self.head

        while cur != None:
            pass
        

N = int(sys.stdin.readline().strip())
for _ in range(N):
    input_line = sys.stdin.readline().split()
    K = input_line[0]
    foods = input_line[1:]
        