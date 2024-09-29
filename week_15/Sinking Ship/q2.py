from sys import stdin

V = int(input())
data = []

for line in stdin:
    x = line.split()
    data.append(x)

print(data)

from simplePriorityQueue import Simple_Priority_Queue


class state:
    def __init__(self, number):
        self.number = number


def successor(s, get_row):
    succ = []
    for row in range(get_row, len(data)):
        for each in data[row]:
            succ.append(state(each))
        return succ


def cityCompare(x, y):
    return x.number > y.number


pq = Simple_Priority_Queue(cityCompare)
s = state(0)
temp = []
get_row = 0
count = 0
while count < V:
    for u in successor(s, get_row):
        pq.enqueue(u)
    s = pq.dequeue()
    if s.number not in temp:
        temp.append(int(s.number))
        count += 1
    get_row += 1

print(temp)
print(sum(temp))