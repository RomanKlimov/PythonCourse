f = open('romeo.txt')
counts = dict()

for line in f:
    line = line.lower()
    words = line.split()

    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
for word in counts:
    print(word + ' ' + str(counts[word]))
