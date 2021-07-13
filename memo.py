# 경섭 4_4
file_name = "sequence.nucleotide.fasta"

ti = ""
seq = list()
re_seq = list()

with open(file_name, "r") as handle:
    for line in handle:
        if line.startswith(">"):
            ti = line
        else:
            seq.append(line.strip())

    seq_s = "".join(seq)

seq_s_rev = seq_s[::-1]

# print(seq_s_rev)

trans_seq = ""
mrna_dict = {"A": "T", "G": "C", "C": "G", "T": "A"}
for i in seq_s_rev:
    # print(i)
    trans_seq += mrna_dict[i]
# print(trans_seq)


##############
file_name = "sequence.nucleotide.gb"
ti = ""
cnt = 1
seq_li = list()
with open(file_name, "r") as handle:
    for line in handle:
        line = line.strip()
        if line.startswith("LOCUS"):
            ti = line
        if cnt == 2:
            # print(line, end="")
            seq_li.append(line)
        if line.startswith("ORIGIN"):
            cnt += 1
    seq = " ".join(seq_li)


cnt = 0
cnt_row = 0
seq_change = list()
for i_row in range(len(seq_li)):
    row_s = seq_li[i_row].split(" ")
    # print(row_s)
    for i in range(len(row_s)):
        if row_s[i].isalpha():
            seq_change.append(row_s[i])

seq_ch = "".join(seq_change)
# print(seq_ch)

print(">", ti)
print(seq_ch)
