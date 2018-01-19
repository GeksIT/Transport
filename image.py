import turtle
import datetime

turtle.speed(0)
turtle.hideturtle()
L, File = [], open('transport_data.csv', 'r')
File.readline()
for line in File:
    L.append(line[:-1].split(','))

L = [x for x in L if x[4] == '0' or x[4] == '1' or x[4] == '2']
for x in L:
    x[0] = ((float(x[0])) * 10000 - 3.03601016998291e+5)*0.8
    x[1] = ((float(x[1])) * 10000 - 5.9931102752685544e+5)*0.8


# переводим UNIX time в обычное время. Удалить в конечной версии программы
for x in L:
    x.append(datetime.datetime.fromtimestamp(int(x[2])).strftime('%Y-%m-%d %H:%M:%S')[8:])
    # print(x[5])

for i, x in enumerate(L):
    x.append(i)


# Разбиваем данные по ррабочим дням
i, prev, day = 0, L[0][2], [[], [], [], [], []]
for x in L:
    if (int(x[2]) - int(prev)) > 18000:
        i += 1
    day[i].append(x)
    prev = x[2]

# разделение красной и синезелёной ветки
turtle.penup()
turtle.goto(-800, 55)
turtle.pendown()
turtle.goto(800, 55)

turtle.penup()
turtle.goto(-456, -800)
turtle.pendown()
turtle.goto(-456, 800)

# разделение синей и зеленой ветки в левом верхнем углу
turtle.penup()
turtle.goto(-552, -800)
turtle.pendown()
turtle.goto(-552, 800)

turtle.penup()
turtle.goto(-800, 127)
turtle.pendown()
turtle.goto(800, 127)

# Отделение зеленой ветки справа (выселки)
turtle.penup()
turtle.goto(330, -800)
turtle.pendown()
turtle.goto(330, 800)

turtle.penup()
turtle.goto(-800, 127)
turtle.pendown()
turtle.goto(800, 127)


turtle.penup()
turtle.goto(-620, -800)
turtle.pendown()


color = ['red', 'blue', 'green']
for x in L:
    turtle.penup()
    turtle.goto(x[0], x[1])
    turtle.pendown()
    turtle.dot(5, color[int(x[4])])
    # turtle.penup()
    # turtle.goto(0, 340)
    # turtle.pendown()
    # turtle.dot(80, 'white')
    # turtle.write(x[5][3:])
turtle.mainloop()



