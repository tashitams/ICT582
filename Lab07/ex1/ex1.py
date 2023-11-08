file = open('Anthem.txt')
i = 0
for line in file:
    i += 1
    print(f"{i}: {line}", end="")

file.close()
