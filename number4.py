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
counter = dict()
for el in answer:
    if el[0] not in counter:
        counter[el[0]] = 1
    else:
        counter[el[0]] += 1
for el in answer:
    el.append(counter[el[0]])

with open ('game_counter.csv', 'w', newline='', encoding='utf-8') as newfile:
    w = csv.writer(newfile)
    w.writerow(['GameName', 'characters', 'nameError', 'date', 'counter'])
    w.writerows(answer)
