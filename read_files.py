# read files
file = open("file.txt", "r")
f = file.readlines()

newList = []
for line in f:
    newList.append(line.strip())
#        newList.append(line[:-1])
#    else:
#        newList.append(line)

print(newList)
file.close()
