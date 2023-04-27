# dict_opcodes = {"add":"00000", "sub":"00001", "mov":["00010","00011"], "ld":"00100",
#         "st":"00101", "mul":"00110", "div":"00111", "rs":"01000",
#         "ls":"01001", "xor":"01010", "or":"01011", "and":"01100",
#         "not":"01101", "cmp":"01110", "jmp":"01111", "jlt":"11100", "jgt":"11101", "je":"11111", "hlt":"11010"}

dict_opcodes = {"add":"00000", "sub":"00001", "mov":"00011", "ld":"00100",
        "st":"00101", "mul":"00110", "div":"00111", "rs":"01000",
        "ls":"01001", "xor":"01010", "or":"01011", "and":"01100",

dict_reg = {"R0":"000", "R1":"001","R2":"010","R3":"011","R4":"100", "R5":"101","R6":"110", "FLAGS":"111"}

with open("input.txt", "r") as f1:
    open("output.txt", "w") 
    for lines in f1.readlines():

        line = lines[:-1].split(" ")
        new_str = ''
        single_line = ''

        for i in line:

            if i == '':
                break

            if i.lower() in dict_opcodes:
                single_line += dict_opcodes[i]

            if i.lower() in dict_reg:
                single_line += dict_reg[i]

            if i[0] == '$':
                single_line += str(int(bin(i[1:])))

        unused = 16 - len(single_line)
        str_final = single_line[0:5] + ('0'*unused) + (single_line[5:])
        new_str += str_final + '\n'
        with open("output.txt", "a") as f2:
            f2.write(new_str)
