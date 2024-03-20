import csv

with open ('game.txt', encoding='utf-8') as file:
    a = file.readline()
    reader = []
    for i in file:
        st = [k for k in i.split('$')]
        if "\n" in st[-1]:
            st[-1] = st[-1].replace("\n", '')
        reader.append(st)
    answer = reader[1:]
for el in answer:
    if '55' in el[2]:
        print(f'У персонажа {el[1]} в игре {el[0]} нашлась ошибка с кодом: {el[2]}. Дата фиксации: {el[3]}')
        el[2] = 'Done'
        el[3] = '0000-00-00'
with open ('game_new.csv', 'w', newline='', encoding='utf-8') as newfile:
    w = csv.writer(newfile)
    w.writerow(['GameName', 'characters', 'nameError', 'date'])
    w.writerows(answer)
