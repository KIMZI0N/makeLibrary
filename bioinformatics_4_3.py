fr = open("sequence.protein.gb", "r")
lines = fr.readlines()
fr.close()
s = []
for i in range(len(lines)):
    if lines[i].startswith("LOCUS"):
        title = lines[i]
    elif lines[i].startswith("ORIGIN"):
        for j in range(len(lines[i + 1 :])):  # ORIGIN 다음 행부터 마지막 행까지 for문
            s.append(lines[i + 1 + j])  # s라는 list에 string 추가.
        seq = "".join(s)  # list를 string으로.
ls = []
result = ""
for i in range(len(seq)):
    if seq[i].isalpha():
        ls.append(seq[i])
        result = "".join(ls)
j = 0
r = int(len(result) / 70) + 1
for i in range(r):
    print(result[j : j + 70])
    j += 70
