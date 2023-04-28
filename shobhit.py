dict_opcodes = {"add":"00000", "sub":"00001", "mov": ["00010", "00011"], "ld":"00100", "st":"00101", 
                "mul":"00110", "div":"00111", "rs":"01000", "ls":"01001", "xor":"01010", 
                "or":"01011", "and":"01100", "not":"01101", "cmp":"01110", "jmp":"01111", 
                "jlt":"11100", "jgt":"11101", "je":"11111", "hlt":"11010","addf":"10000",
                "subf":"10001"}

dict_reg = {"R0":"000", "R1":"001", "R2":"010", "R3":"011", "R4":"100", "R5":"101", "R6":"110",
            "FLAGS":"111"}
list_var = []
dict_var = {}
list_assembler = []
dict_assembler = {}
def dec_bin(dec):
    dec = int(dec)
    binary = ''
    while dec != 0:
        if dec % 2 == 0:
            binary += '0'
        if dec % 2 == 1:
            binary += '1'
        dec = dec // 2

    unused = 7 - len(binary)
    binary = binary[-1::-1]
    binary = '0' * unused + binary
    return binary

with open("input123.txt", "r") as f1:
    count=0
    for lines in f1.readlines():
        a = lines.strip(' ')
        b = a.strip('\t')
        c = b.strip('\n')
        line = c.split(" ")

        for i in line:
            if i == '':
                break
            if i == "var":
                list_var.append(line[1])
            if i in dict_opcodes:
                count+=1
f1.close()
print(f"The number of instructions are: {count}")
count2=count
for item in list_var:
    dict_var[item]=dec_bin(count2)
    count2+=1
print(dict_var)
with open("input123.txt", "r") as f1:
    open("output123.txt", "w") 
    for lines in f1.readlines():
        a = lines.strip(' ')
        b = a.strip('\t')
        c = b.strip('\n')
        #q = lines[:-1]
        line = c.split(" ")
        str_final = ''
        single_line = ''
        new_str = ''

        for i in line:
            #print(i)
            if i == '':
                break
            if i == "var":
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

            if i[0] == '$':
                single_line += dec_bin(i[1::1])

            if i in dict_var:
                single_line += dict_var[i]

        unused = 16 - len(single_line)
        str_final = single_line[0:5] + ('0'*unused) + (single_line[5:])
        new_str += str_final + '\n'
        if new_str!="0000000000000000\n":
            list_assembler.append(str_final)
            with open("output123.txt", "a") as f2:
                f2.write(new_str)
          
f1.close()
f2.close()
for i in range(count):
    dict_assembler[dec_bin(i)]=list_assembler[i]
print(dict_assembler)