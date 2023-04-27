dict_opcodes = {"add":"00000", "sub":"00001", "mov":["00010","00011"], "ld":"00100",
        "st":"00101", "mul":"00110", "div":"00111", "rs":"01000",
        "ls":"01001", "xor":"01010", "or":"01011", "and":"01100",
        "not":"01101", "cmp":"01110", "jmp":"01111", "jlt":"11100", "jgt":"11101", "je":"11111", "hlt":"11010"}

# dict_opcodes = {"add":"00000", "sub":"00001", "mov":"00011", "ld":"00100",
#         "st":"00101", "mul":"00110", "div":"00111", "rs":"01000",
#         "ls":"01001", "xor":"01010", "or":"01011", "and":"01100",
#         "not":"01101", "cmp":"01110", "jmp":"01111", "jlt":"11100", "jgt":"11101", "je":"11111", "hlt":"11010"}

dict_reg = {"R0":"000", "R1":"001","R2":"010","R3":"011","R4":"100", "R5":"101","R6":"110", "FLAGS":"111"}

def dec_bin(dec):
    dec = int(dec)
    binary = ''
    while (dec!=0):
        if dec%2==0:
            binary += '0'
        if dec%2==1:
            binary += '1'
        dec = dec//2

    unused = 7 - len(binary)
    binary = binary[-1::-1]
    binary = '0'*unused + binary
    return binary

with open("input.txt", "r") as f:

    new_str = ''
    for lines in f.readlines():
        lines.strip(' \n\t')
        line = lines.split(" ")
        str_final = ''
        single_line = ''

        for i in line:
            # print(i)
            if i == '':
                break

            if i in dict_opcodes:

                if i == "mov":
                    if line[-1][0] == '$':
                        single_line += dict_opcodes[i][0]
                    else:
                        single_line += dict_opcodes[i][1]
                else:
                    single_line += dict_opcodes[i]


            if i in dict_reg:
                single_line += dict_reg[i]

            if i[0] =='$' :
                single_line += dec_bin(i[1::1])

        unused = 16 - len(single_line)
        str_final = single_line[0:5] + ('0'*unused) + (single_line[5:])
        new_str += str_final + '\n'

# print(new_str)
with open("output.txt", "w") as f:
    f.write(new_str)