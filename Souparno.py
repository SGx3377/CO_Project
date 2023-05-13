# Error handling for Halt
# List to go in function is list_of_assembly_inst
def halt_error(list):
    l = list
    np = 0
    for i in range (len(l)):
        if l[i][1]!='hlt':
            np += 1
        else:
            if i!=len(l)-1:
                print(f'Halt is not present at the right place, it is present in line {i+1}')
                np = 0
                break
            else:
                np = 0
                break
    if np!=0:
        print(f'Halt is not present')