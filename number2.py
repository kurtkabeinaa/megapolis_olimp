with open ('game.txt', encoding='utf-8') as file:
    a = file.readline()
    reader = []
    for i in file:
        st = [k for k in i.split('$')]
        if "\n" in st[-1]:
            st[-1] = st[-1].replace("\n", '')
        reader.append(st)
    answer = reader[1:]
