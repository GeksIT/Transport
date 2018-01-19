import datetime
import random


def ranged(point1, point2):
    return (float(point2[0]) - float(point1[0]))**2 + (float(point2[1]) - float(point1[1]))**2


L, File, result = [], open('transport_data.csv', 'r'), []
File.readline()
for line in File:
    L.append(line[:-1].split(','))
ssum = 0
for x in L:
    if x[4] == '?':
        ssum += 1
print(ssum)


# переводим UNIX time в обычное время. Удалить в конечной версии программы
for x in L:
    x.append(datetime.datetime.fromtimestamp(int(x[2])).strftime('%Y-%m-%d %H:%M:%S')[8:])
    # print(x[5])

for i, x in enumerate(L):
    x.append(i)

# Раскидываем очевидные точки
for x in L:
    if x[4] == '-' or x[4] == '?':
        if float(x[0]) < 30.3145016998291 and float(x[1]) < 59.936602752685545:
            if x[4] == '?':
                result.append(x)
            x[4] = '0'
        elif float(x[0]) < 30.304901699829102 and float(x[1]) > 59.936602752685545 and float(x[1]) < 59.943502752685546:
            if x[4] == '?':
                result.append(x)
            x[4] = '1'
        elif (float(x[0]) > 30.393101699829103 and float(x[1]) < 59.94380275268555) or (float(x[0]) < 30.304901699829102 and float(x[1]) > 59.943502752685546):
            if x[4] == '?':
                result.append(x)
            x[4] = '2'
        elif float(x[0]) < 30.26:
             if x[4] == '?':
                 result.append(x)
             x[4] = '1'


map_e = {}
for x in L:
    if (x[4] == '0' or x[4] == '1' or x[4] == '2') and (x[0], x[1]) not in map_e:
        map_e[(x[0], x[1])] = x[2:]

# print(map_e)


for x in L:
    if (x == '-' or x == '?') and (x[0], x[1]) in map_e:
        if x[4] == '?':
            result.append(x)
            result[-1][4] = map_e[(x[0], x[1])][4]
        x[4] = map_e[(x[0], x[1])][4]


# Начинаем метод ближайших соседей

ssum = 0
count = 0
x1 = []
while count < len(L):
    x2 = x1
    x1 = [x for x in L if x[2] == L[count][2]]
    if x2:
        for xx1 in x1:
            if xx1[4] == '?' or xx1[4] == '-':
                aa = [x + [ranged(x, xx1)] for x in x2]
                aa.sort(key=lambda p: p[7])
                if xx1[4] == '?':
                    result.append(xx1)
                    result[-1][4] = aa[0][4]
                xx1[4] = aa[0][4]

    else:
        for x in x1:
            if x[4] == '?' or x[4] == '-':
                if x[4] == '?':
                    result.append(x)
                x[4] = str(random.randrange(0, 3, 1))
    count += len(x1)
print(result)

result.sort(key=lambda p: p[6])
print(len(result))

WFile = open('result.txt', 'w')
for x in result:
    WFile.write(str(x[4]) + '\n')
WFile.close()

