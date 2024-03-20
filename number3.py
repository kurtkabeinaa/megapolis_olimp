with open ('game.txt', encoding='utf-8') as file:
    a = file.readline()
    reader = []
    for i in file:
        st = [k for k in i.split('$')]
        if "\n" in st[-1]:
            st[-1] = st[-1].replace("\n", '')
        reader.append(st)
    answer = reader[1:]
character_name = input()
while character_name != 'game':
    n = 0
    for el in answer:
        if n == 5:
            print('и др.')
            break
        if el[1] == character_name and n == 0:
            print(f'Персонаж {character_name} встречается в играх:')
            print(el[0])
            n += 1
        elif el[1] == character_name and n != 0:
            print(el[0])
            n += 1
    else:
        print('Этого персонажа не существует')
    character_name = input()