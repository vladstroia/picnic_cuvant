with open("cuvinte.txt", "r") as f:
    cuvinte = f.readlines()
contents = ""
for i in cuvinte:
    nr_de_litere = str(len(i)-1)
    nume_fisier = nr_de_litere + "lit.txt"
    with open(nume_fisier, "a") as f:
        f.write(i)