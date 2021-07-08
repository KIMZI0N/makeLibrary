with open("sequence.protein.2.fasta", "r") as handle:
    for i in range(2):
        data = handle.readline()
    print("The second line is: ", data)

"""
fr = open("sequence.protein.2.fasta", "r")
lines = fr.readlines()
line_count = 0
for line in lines:
    line = line.strip()
    if line_count == 1:
        break
    line_count

"""
