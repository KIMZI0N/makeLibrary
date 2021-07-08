with open("sequence.protein.fasta", "r") as fr:
    data = fr.read()
    print(data)
"""
fr = open("sequence.protein.fasta", "r")
for line in fr:
    line = line.strip()
    if line == "": #공백 예외 처리
        continue
    print(line)
fr.close()
"""
