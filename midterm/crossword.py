
def read_crossword(path):
    f = open(path, encoding='utf-8')
    cross = f.readlines()
    f.close()
    return [s[:-1] for s in cross]

def print_crossword(cross):
    for i in range(1,len(cross),2):
        cross[i] = cross[i].split()
        cross[i] = [j[1:-1].split() for j in cross[i]]
        cross[i] = [(int(j[0][0]),int(j[0][2])) for j in cross[i]]



    return cross

print(print_crossword(read_crossword('crossword_3.txt')))
