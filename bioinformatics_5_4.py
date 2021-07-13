fr = open("sequence.nucleotide.gb", "r")
ls = []
s = ""
p = a = 0
for line in fr:
    if "CDS" in line[0:8]:
        p = 1
    elif (p == 1) & ("exon" in line[0:9]):
        p = 0
    if p == 1:
        if "translation" in line:
            a = 1
    if (p == 1) & (a == 1):
        line = line.strip()
        ls.append(line)
s = "".join(ls)
s = s.replace('/translation="', "").replace('"', "")
print(s)
fr.close()
