def b_c(str1):
    a = str1
    for i in range(len(a)): #to remove all trailing white spaces
        if a[i].isnumeric(): 
            a = a[i::]
            break

    list_opcodes = {"00000","00001","00010","00011","00100","00101", "00110", "00111","01000", "01001", "01010","01011", "01100",
        "01101", "01110", "01111", "11100", "11101", "11111", "11010"}

    list2 = ['r0', 'r1','r2','r3','r4','r5','r6','r7']
    list1 = a.split(' ')
    
    if list1[0] not in list_opcodes:
        return "ERROR : OPCODE NOT IN THE GIVEN ISA"

    if list1[2].isnumeric():
        if int(list1[2])>127:
            return 'ERROR : IMMIDIATE VALUE GREATER THAN 127'

        if list1[1].lower() not in list2:
            return 'ERROR : REGISTER NOT IN THE GIVEN ISA'
    else:
        if list1[1].lower() not in list2 or list1[2].lower() not in list2:
            return 'ERROR : REGISTER NOT IN THE GIVEN ISA'

# print(b_c("  00111 R0 R1 "))
# return none if no error