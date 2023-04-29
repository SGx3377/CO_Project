dict_opcodes = {"add":"00000", "sub":"00001", "mov": ["00010", "00011"], "ld":"00100", "st":"00101", 
                "mul":"00110", "div":"00111", "rs":"01000", "ls":"01001", "xor":"01010", 
                "or":"01011", "and":"01100", "not":"01101", "cmp":"01110", "jmp":"01111", 
                "jlt":"11100", "jgt":"11101", "je":"11111", "hlt":"11010","addf":"10000",
                "subf":"10001"}

dict_reg = {"R0":"000", "R1":"001", "R2":"010", "R3":"011", "R4":"100", "R5":"101", "R6":"110",
            "FLAGS":"111"}
reg_values = {"r0":0, "r1":0, "r2":0, "r3":0, "r4":0, "r5":0, "r6":0, 
        "flag":"0000000000000000"} #Register value is 16 bits (hence range [0,65535] (0 to 2^16-1))
list_of_assembly_inst= []
list_of_firstwords = []
list_var = []
dict_var = {}
list_jump = ["jmp","jlt","jgt","je"]
list_label = []
list_label2 = []
dict_label = {}
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
    for lines in f1.readlines():
        a = lines.strip(' ')
        b = a.strip('\t')
        c = b.strip('\n')
        line = c.split(" ")
        list_of_assembly_inst.append(line)
f1.close()
print(list_of_assembly_inst)
for item in list_of_assembly_inst:
    list_of_firstwords.append(item[0])
# print(list_of_firstwords)
count=0
for item in list_of_assembly_inst:
    if item[0] == '':
        break
    if item[0] == "var":
        list_var.append(item[1])
    if item[0] in list_jump:
        list_label.append(item[1])
        list_label2.append(item[1]+":")        
        count+=1
    if item[0] not in list_jump and item[0] in dict_opcodes:
        count+=1
    if item[0] in list_label2:
        count+=1
# print(list_label)
# print(list_label2)
print(f"The number of instructions are: {count}")
count2=count
for item in list_var:
    dict_var[item]=dec_bin(count2)
    count2+=1
print(dict_var)
for item in list_of_assembly_inst:
    if item[0] in list_label2:
        dict_label[item[0].replace(":","")]=dec_bin(list_of_firstwords.index(item[0])-len(list_var))
# print(dict_label)
with open("input123.txt", "r") as f1:
    open("myoutput.txt", "w") 
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

            if i in list_label:
                single_line += dict_label[i]

        unused = 16 - len(single_line)
        str_final = single_line[0:5] + ('0'*unused) + (single_line[5:])
        new_str += str_final + '\n'
        if new_str!="0000000000000000\n":
            list_assembler.append(str_final)
            with open("myoutput.txt", "a") as f2:
                f2.write(new_str)        
f1.close()
f2.close()
for i in range(count):
    dict_assembler[dec_bin(i)]=list_assembler[i]
print(dict_assembler)