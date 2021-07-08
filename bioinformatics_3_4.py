fr = open("sequence.protein.fasta", "r")
lines = fr.readlines()
fr.close()

fw = open("sequence.protein.2.fasta", "w")
for line in lines:
    fw.write(line)
fw.close()

"""
fr = open("sequence.protein.fasta", "r")
lines = fr.readlines()
seq_list = list()
for line in lines:
    line = line.strip()
    if line == "":
        continue
    seq_list.append(line)
fr.close()

seq = "\n".join(seq_list)
fw = open("sequence.protein.2.fasta", "w")
fw.write("%s\n" % (seq))
fw.close()
"""
