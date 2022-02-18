import sys
maze1 = sys.argv[1]
maze_health1 = sys.argv[2]
health_time = sys.argv[3]
output = sys.argv[4]

list1 = list()
with open(maze1) as file:
    for line in file.readlines():
        line = line.replace("\n", "")
        for value in line:
            list1.append(value)

list1 = [list1[i: i+len(line)] for i in range(0, len(list1), len(line))]

list3 = list()
for x in range(len(list1)):
    list3.append([0]*len(list1[0]))
for i in list1:
    if "S" in i:
        a = list1.index(i)
        b = i.index("S")
        list3[a][b] = 'S'

def maze(x,y):
    try:
        if list1[x][y] == "F":
            list3[x][y] = "F"
            return True
        if list1[x][y] == "W":
            return False
        list1[x][y] = 'W'
        if maze(x, y-1) and 0 < y:
            list3[x][y] = int('1')
            return True
        if maze(x, y + 1) and y+1 < len(i):
            list3[x][y] = int('1')
            return True
        if maze(x - 1, y) and 0 < x:
            list3[x][y] = int('1')
            return True
        if maze(x + 1, y) and x + 1 < len(list1):
            list3[x][y] = int('1')
            return True
        if list1[x][y - 1] == "F" and 0 < y:
            list3[x][y] = "F"
            return True
        if list1[x][y+1] == "F" and y+1 < len(i):
            list3[x][y] = "F"
            return True
        if list1[x-1][y] == "F" and 0 < x:
            list3[x][y] = "F"
            return True
        if list1[x+1][y] == "F" and x + 1 < len(list1):
            list3[x][y] = "F"
            return True
        list1[x][y] = "P"
        list3[x][y] = 0
        return False
    except IndexError:
        pass
maze(a,b)
list3[a][b] = 'S'

list2 = list()
with open(maze_health1) as file:
    for line in file.readlines():
        line = line.replace("\n", "")
        for value in line:
            list2.append(value)

list2 = [list2[i: i + len(line)] for i in range(0, len(list2), len(line))]

list4 = list()
for x in range(len(list2)):
    list4.append([0]*len(list2[0]))

for i in list2:
    if "S" in i:
        n, m = list2.index(i), i.index("S")
        list4[n][m] = "S"

health_time = int(health_time)
health = health_time
def maze_health(x, y,health):
    try:
        if list2[x][y] == "F":
            list4[x][y] = "F"
            return True
        if list2[x][y] == "W":
            return False
        if health < 0:
            return False
        if list2[x][y] == "H":
            health = health_time
            list2[x][y] = "P"
            list4[x][y] = 1
        list2[x][y] = "W"
        if list2[x][y] == 'W':
            health -= 1
        if maze_health(x, y + 1, health) and y+1 < len(i):
            list4[x][y] = 1
            return True
        if maze_health(x, y-1, health) and 0 < y:
            list4[x][y] = 1
            return True
        if maze_health(x - 1, y, health) and 0 < x:
            list4[x][y] = 1
            return True
        if maze_health(x + 1, y, health) and x + 1 < len(list2):
            list4[x][y] = 1
            return True
        if list2[x][y - 1] == "F" and 0 < y:
            list4[x][y] = "F"
            health -= 1
            return True
        if list2[x][y+1] == "F" and y+1 < len(i):
            list4[x][y] = "F"
            health -= 1
            return True
        if list2[x-1][y] == "F" and 0 < x:
            list4[x][y] = "F"
            health -= 1
            return True
        if list2[x+1][y] == "F" and x + 1 < len(list2):
            list4[x][y] = "F"
            health -= 1
            return True
        list2[x][y] = "P"
        list4[x][y] = 0
        health = health_time
        return False
    except IndexError:
        pass
maze_health(n,m, health)
list4[n][m] = "S"

with open(output, "w") as file:
    for item in list3:
        item = str(item)[1:-1]
        item = item.replace("'", "")
        file.write("".join(item))
        file.write("\n")
    file.write("\n")
    for item in list4:
        item = str(item)[1:-1]
        item = item.replace("'", "")
        file.write("".join(item))
        file.write("\n")
