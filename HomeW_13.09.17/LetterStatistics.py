file = open('romeo.txt')
counts = dict()

for line in file:
    line = line.replace(' ', '')
    line = line.lower()
    line = line.strip()  # убираем весь мусор
    for char in line:
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1
for char in counts:
    print(char + ' ' + str(counts[char]))
