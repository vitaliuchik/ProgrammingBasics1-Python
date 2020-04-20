menu = []
while True:
    line = input()
    if line:
        menu.append(line.split())
    else:
        break

menu = [[menu[i][0], float(menu[i][2])/float(menu[i][1])] for i in range(len(menu))]

menu.sort(key=lambda x: x[1])
for el in menu:
    print(el[0], end=' ') 


