# 0~11번쨰 행까지 검사해서 TITLE인지 공백인지 다른 문자인지 확인
fr = open("sequence.nucleotide.gb", "r")
p = 0
s = ""
ls = []
for line in fr:
    ch = line[0:12]  # 공백 또는 대문자(제목?) 부분
    if "TITLE" in ch:
        p = 1
    elif ch == "            ":
        pass
    elif "JOURNAL" in ch:
        p = 2
    else:
        p = 0

    if p == 1:
        line = line.replace("\n", " ")
        s += line
    else:
        pass
fr.close()
s = s.split("TITLE")
print("TITLE", end="")
for i in s:
    i = i.replace("            ", "")
    print(i)
