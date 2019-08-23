try:
    f = open("config.txt", "r")
except:
    f = open("../config.txt", "r")
strings = [line for line in f]
f.close()

for line in strings:
    if line.startswith("name="):
        name = line[5:]
    elif line.startswith("uuid="):
        UUID = line[5:]
