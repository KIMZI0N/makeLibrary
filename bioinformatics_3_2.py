with open("title.txt", "r") as handle:
    data = handle.read()
    print(data)

"""
fr = open("title.txt", "r")
# lines = fr.readlines() -> 이렇게 하지 않기.
for line in fr:
    line = line.strip()  # line은 string
    break  # break가 있어서 for문이 한번만 반복됨.
    # break없으면 맨 마지막 줄이 line에 저장됨.
fr.close()
print("The first line is: %s" % (line))
"""
