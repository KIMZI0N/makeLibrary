list = []
fr = open("sequence.nucleotide.fasta", "r")
p = 0
for line in fr:
    line = line.strip()
    if p == 1:
        list.append(line)
    p = 1
seq = "".join(list)
fr.close()
r = int(len(seq) / 3) + 1
for i in range(r):
    j = i * 3
    print(seq[j : j + 3])
