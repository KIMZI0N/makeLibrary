codon_dic = {
    "TTT": "F",
    "TTC": "F",
    "TTA": "L",
    "TTG": "L",
    "TCT": "S",
    "TCC": "S",
    "TCA": "S",
    "TCG": "S",
    "TAT": "Y",
    "TAC": "Y",
    "TAA": "*",
    "TAG": "*",
    "TGT": "C",
    "TGC": "C",
    "TGA": "*",
    "TGG": "W",
    "CTT": "L",
    "CTC": "L",
    "CTA": "L",
    "CTG": "L",
    "CCT": "P",
    "CCC": "P",
    "CCA": "P",
    "CCG": "P",
    "CAT": "H",
    "CAC": "H",
    "CAA": "Q",
    "CAG": "Q",
    "CGT": "R",
    "CGC": "R",
    "CGA": "R",
    "CGG": "R",
    "ATT": "I",
    "ATC": "I",
    "ATA": "I",
    "ATG": "M",
    "ACT": "T",
    "ACC": "T",
    "ACA": "T",
    "ACG": "T",
    "AAT": "N",
    "AAC": "N",
    "AAA": "K",
    "AAG": "K",
    "AGT": "S",
    "AGC": "S",
    "AGA": "R",
    "AGG": "R",
    "GTT": "V",
    "GTC": "V",
    "GTA": "V",
    "GTG": "V",
    "GCT": "A",
    "GCC": "A",
    "GCA": "A",
    "GCG": "A",
    "GAT": "D",
    "GAC": "D",
    "GAA": "E",
    "GAG": "E",
    "GGT": "G",
    "GGC": "G",
    "GGA": "G",
    "GGG": "G",
}
list = []
fr = open("sequence.nucleotide.fasta", "r")
p = 0
for line in fr:
    line = line.strip()
    if p == 1:
        list.append(line)
    p = 1
seq = "".join(list)  # base만 있는 sequence
fr.close()

ls = []
r1 = int(len(seq) / 3)
for i in range(r1):
    j = i * 3
    ls.append(seq[j : j + 3])  # codon단위로 ls라는 list에 저장.

r2 = int(len(ls) / 20)
for s in range(r2):
    for i in range(20 * s, 20 * s + 20):
        print(ls[i], end="")
    print()
    for j in range(20 * s, 20 * s + 20):
        print(codon_dic[ls[j]], end="  ")
    print()
str = "".join(ls[r2 * 20 :])
print(str)
for i in ls[r2 * 20 :]:
    print(codon_dic[i], end="  ")
print()

# s_cod = ""
# s_ami = ""
# s_cod = "".join(ls[0:20])

# print(s_cod)
# print(s_ami)

# while문
# i = 0
# while True:
#     print(ls[i],end='')
#     i +=1
#     if i == 20:
#         print()
#         print(codon_dic[j],end='')

#     print(codon_dic[])
#     i += 20
#     if i == 20:
#         print()
#         break
#     continue
