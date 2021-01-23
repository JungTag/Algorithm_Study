import sys
import heapq

class Node:
    def __init__(self, key, weight):
        self.key = key
        self.weight = weight
        self.next = None
    def __str__(self):
        return str(self.key)

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        v = self.head
        while v:
            print((v.key, v.weight), "->", end=" ")
            v = v.next
        print("None")

    def pushFront(self, key, weight):
        new_node = Node(key, weight)
        new_node.next = self.head
        self.head = new_node
    
    def pushBack(self, key, weight):
        new_node = Node(key, weight)
        if self.head == None:
            self.head = new_node
        else:
            tail = self.head
            while tail.next != None:
                tail = tail.next
            tail.next = new_node
    
    def search(self, key):
        v = self.head
        while v:
            if v.key == key:
                return v.key
            v = v.next
        return None
    
    def get_weight(self, key):
        v = self.head
        while v:
            if v.key == key:
                return v.weight
            v = v.next
    
    def get_nodes(self):
        nodes = []
        v = self.head
        while v:
            nodes.append(v.key)
            v = v.next
        return nodes

    
V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
G = [SinglyLinkedList() for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    G[u].pushFront(v, w)

def Dijkstra(Graph):
    dist = [float('inf') for _ in range(V+1)]
    dist[1] = 0 # 시작 노드의 거리는 0으로 설정
    Q = []
    for v in range(V+1):
        Q.append((dist[v], v))
    heapq.heapify(Q)
    while Q:
        result = heapq.heappop(Q)
        u = result[1]
        for v in G[u].get_nodes():
            if G[u].search(v) != None:
                if dist[v] > dist[u] + G[u].get_weight(v): # relax
                    old_dist = dist[v]
                    dist[v] = dist[u] + G[u].get_weight(v)
                    Q.remove((old_dist, v))
                    Q.append((dist[v], v))
                    heapq.heapify(Q)
    for i in range(1, V+1):
        if dist[i] == float('inf'):
            print("INF")
        else:
            print(dist[i])

Dijkstra(G)
