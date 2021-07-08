list = []
fr = open("sequence.protein.2.fasta", "r")
for line in fr:
    line = line.strip()
    if line[0] == ">":
        title = line
    else:
        list.append(line)
seq = "".join(list)
print(f"title: {title}")
print(f"seq: {seq}")
fr.close()
