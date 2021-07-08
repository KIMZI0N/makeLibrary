fr = open("sequence.protein.gb", "r")
lines = fr.readlines()
title = lines[0]
ls = []
# seq라는 변수에 저장해서 프린트해야함!!
string = ""
print(f"title: {title}")
for i in range(1, len(lines)):
    if lines[i].startswith("ORIGIN"):
        print("seq:", end="")
        for j in range(len(lines[i + 1 :])):
            s = lines[i + 1 + j]
            s = s.strip()
            print(s)
fr.close()

#'>'로 구분하기
# string보단 list에 담는게 메모리상으로 더 효율적임.
# seq = ''.join(seq_list) -> list에 담고 한 번에 string으로 바꿔주기
