import itertools
litere = input("Care sunt literele?")
nr_lit = int(input("Cate litere?"))
file_name ="cuv/" + str(nr_lit) + "lit.txt"
with open(file_name, "r") as f:
    contents = f.readlines()        
cuvinte = list(itertools.permutations(litere, nr_lit))


for i in cuvinte:
    i = "".join(i) + "\n"
    if i in contents:
        print(i)
