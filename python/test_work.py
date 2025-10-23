with open(
    "C:\\Users\\user\\Desktop\\ворк\\pass.txt", "r", encoding="utf-8"
) as file_pass, open(
    "C:\\Users\\user\\Desktop\\ворк\\pass_ready.txt", "w", encoding="utf-8"
) as file_pass_ready:
    for line in file_pass.readlines():
        line = line.strip().split()
        line[4] = line[4][:4] + " " + line[4][4:]

        if int(line[4][2:4]) >= 12:
            line.append("25.11.20" + line[4][2:4])
        else:
            line.append("25.11.2012")

        file_pass_ready.write(" ".join(line) + "\n\n\n\n")
