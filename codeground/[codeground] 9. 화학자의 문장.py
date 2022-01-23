import sys

inf = sys.stdin

char_list = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al",
             "Si", "P", "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe",
             "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr",
             "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb",
             "Te", "I", "Xe", "Cs", "Ba", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au",
             "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Rf", "Db", "Sg",
             "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Fl", "Lv", "La", "Ce", "Pr", "Nd",
             "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Ac",
             "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md",
             "No", "Lr"]

for i in range(len(char_list)):
    char_list[i] = char_list[i].lower()

char_list.sort()


def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return True
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return False

T = inf.readline()

for t in range(0, int(T)):
    Answer = 0
    input_str = inf.readline()
    input_str = input_str.replace('\n','')
    label = [0 for _ in range(len(input_str) + 1)]
    label[0] = True
    label[1] = binary_search(input_str[0:1], char_list)
    
    for i in range(2, len(input_str) + 1):
        label[i] = ((binary_search(input_str[i-1:i], char_list) & label[i-1]) | (binary_search(input_str[i-2:i], char_list) & label[i-2]))
        
    if label[len(input_str)]:
         Answer = "YES"
    else:
         Answer = "NO"
    print('Case #%d' %(int(t)+1))    
    print(Answer)


