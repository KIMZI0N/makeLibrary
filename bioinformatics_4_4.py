# 겹치는 코드 합쳐보기..!
while True:
    inFi = input("Enter input file: ")
    if inFi == "XXX":
        break
    ouFi = input("Enter output file: ")
    print(
        "Option-1) Read a FASTA format DNA sequence file and make a reverse sequence file."
    )
    print(
        "Option-2) Read a FASTA format DNA sequence file and make a reverse complement sequence file."
    )
    print("Option-3) Convert GenBank format file to FASTA format file.")
    opt = input("Select the option: ")

    if opt == "1":
        # inFi로 받은 파일명. inFi의 seq구하기.
        # seq의 역순을 새로운 파일(파일명은 ouFi로)에 write하기.
        list = []
        fr = open(inFi, "r")
        for line in fr:
            line = line.strip()
            if line.startswith(">"):
                title = line
            else:
                list.append(line)
            seq = "".join(list)
        fr.close()
        seqRev = seq[::-1]
        fw = open(ouFi, "w")
        fw.write(f"{title}\n{seqRev}")
        fw.close()

    elif opt == "2":
        # inFi로 받은 파일명. inFi의 seq구하기.
        # seq의 역순 구하고, 상보적으로 replace하기.
        # 결과값을 새로운 파일(이름은 ouFi로 )에 write하기.
        list = []
        fr = open(inFi, "r")
        for line in fr:
            line = line.strip()
            if line.startswith(">"):
                title = line
            else:
                list.append(line)
            seq = "".join(list)
        fr.close()
        seqRev = seq[::-1]
        seqRev = (
            seqRev.replace("A", "t")
            .replace("T", "a")
            .replace("C", "g")
            .replace("G", "c")
        )
        seqRev = seqRev.upper()
        fw = open(ouFi, "w")
        fw.write(f"{title}\n{seqRev}")
        fw.close()

    elif opt == "3":
        # sequence.nucleotide.gb
        # new.sequence.nucleotide.fasta
        # inFi는 genebank파일이고 ouFi는 gb를 fasta로 바꾼 fasta파일.
        # genebank의 첫줄->fasta의 >로 시작하는 첫줄 -> 변수 title
        # gb의 origin 이후-> fasta의 두번째줄부터 끝까지 -> 변수 seq에 넣기.
        fr = open(inFi, "r")
        lines = fr.readlines()
        fr.close()
        s = []
        for i in range(len(lines)):
            if lines[i].startswith("LOCUS"):
                title = lines[i]
            elif lines[i].startswith("ORIGIN"):
                for j in range(
                    len(lines[i + 1 :])
                ):  # ORIGIN 다음 행부터 마지막 행까지 for문
                    s.append(lines[i + 1 + j])  # s라는 list에 string 추가.
                seq = "".join(s)  # list를 string으로.
                ls = []
                result = ""
                for i in range(len(seq)):
                    if seq[i].isalpha():
                        ls.append(seq[i])
                        result = "".join(ls)
        fw = open(ouFi, "w")
        fw.write(f">{title}\n{result}")
        fw.close()
    else:
        print("retry!")
        continue
