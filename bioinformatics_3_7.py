list = []
fr = open("sequence.protein.2.fasta", "r")
for line in fr:
    line = line.strip()
    if line[0] == ">":
        title = line
    else:
        list.append(line)
seq = "".join(list)
fr.close()


while True:
    pos = input("Position: ")
    if pos == "XXX":
        print("Okay, I will stop.")
        break
    elif 1 <= int(pos) <= (len(seq) - 2):
        pos = int(pos)
        ami = seq[pos - 1 : pos + 2]
        print(ami)
    else:
        print("wrong position!")
