dict = {}

while True:
    codB = input("Enter three-base codon to build: ")
    if codB != "XXX":
        ami = input("Enter amino acid: ")
        dict[codB] = ami
        continue
    elif codB == "XXX":
        print("Okay, I will switch.")
        while True:
            codS = input("Enter three-base codon to search: ")
            if codS in dict.keys():
                print(f"Amino acid for {codS}: ", dict[codS])
            elif codS == "XXX":
                print("Okay, I will stop.")
                break
        break
