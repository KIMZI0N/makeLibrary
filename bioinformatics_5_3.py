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

# base만 있는 sequence인 seq
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

# 상보적seq인 seqCom
seqCom = ""
dicB = {"A": "T", "G": "C", "C": "G", "T": "A"}
for i in seq:
    seqCom += dicB[i]

# 상단 출력
for i in range(0, len(seq), 3):
    print(codon_dic[seq[i : i + 3]], end="  ")
print("\n", "", end="")
for i in range(0, len(seq) - 3, 3):
    print(codon_dic[seq[i + 1 : i + 4]], end="  ")
print("\n", " ", end="")
for i in range(0, len(seq) - 3, 3):
    print(codon_dic[seq[i + 2 : i + 5]], end="  ")
print()
print(seq)

# 하단 출력
print(seqCom)
seqComRev = seqCom[::-1]  # seqCom의 역순 string
# 역순 string(seqComRev)에 맞춰 아미노산 매칭하고, 다시 역순으로 print
ls1 = []
ls2 = []
ls3 = []
# 매칭된 아미노산들 list에 저장.
for i in range(0, len(seqComRev), 3):
    ls1.append(codon_dic[seqComRev[i : i + 3]])
for i in range(0, len(seqComRev) - 3, 3):
    ls2.append(codon_dic[seqComRev[i + 1 : i + 4]])
for i in range(0, len(seqComRev) - 3, 3):
    ls3.append(codon_dic[seqComRev[i + 2 : i + 5]])
# list를 string으로
s1 = "  ".join(ls1)
s2 = "  ".join(ls2)
s3 = "  ".join(ls3)
# string을 역순으로(역순 string에 맞춰서 매칭했으니까)
s1Rev = s1[::-1]
s2Rev = s2[::-1]
s3Rev = s3[::-1]
print(" ", s1Rev)
print("   ", s2Rev)
print("  ", s3Rev)
