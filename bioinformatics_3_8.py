fr = open("sequence.protein.2.fasta", "r")
lines = fr.readlines()
title = lines[0]
seq = ""
for i in range(1, len(lines)):
    seq += lines[i]
    seq = seq.strip()
fr.close()

l = []
while True:
    s = input("Searching for: ")
    if s == "XXX":
        print("Okay, I will stop.")
        break
    for i in range(len(seq)):
        if seq[i] == s:
            a = str(i + 1)
            l.append(a)
    string = ", ".join(l)
    print(f"Found at: {string}")

# while True:
#     aa = input("Enter amino acid code: ")
#     if aa == "XXX":
#         print("Okay, I will stop.")
#         break
#     else:
#         found_pos_list = list()
#         i = 1
#         for c in seq:
#             if c == aa:
#                 found_pos_list.append(str(i))
#             i += 1
#         print("Found at: %s" % (",".join(found_pos_list)))
