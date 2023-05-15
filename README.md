# CO_Project
CO Group Project
This repository is a python program of a custom-made assembler designed to translate assembly language code into machine code for a specific 
computer architecture (ISA).
The full code is present in Whole code.py in the main branch.

Description - 
The program will convert an assembly language code to machine language(Binary Format). 
The program is able to handle all the supported instructions of the ISA, labels & variables along with two new instruction (addf and subf)
The program is able to generate errors for different types of invalid instructions along with the line no. in
which the error is encountered.

Input/Output - 
The input for the program has to be done manually from an input file "stdin.txt" which has the assembly language code.
The output will be a file "stdout.txt" that would have the binary format of the respective instructions.

Error Handling - 
The errors present in the assembly code will be printed in the output file "stdout.txt" along with the line number in which the error is
encountered. 
The error handling has been done using IF-ELSE and exit() function.

Extra - 
All the test cases given in SimpleGen, HardGen and CO_Project_Testcases has been tested and all of them gave the right answer
All the testcases are present in one of the branches.

Example (Input file) - 
Assembly Code
var xyz
var abc
l1: mov R0 $5
mov R1 $6
mov R5 FLAGS
l_2:	st R0 xyz
	add R0 R0 R1
	ld R2 abc
	je l1
	jgt l_2
hlt

Binary Format (Output file generated)
0001000000000101
0001000010000110
0001100000101111
0010100000001001
0000000000000001
0010000100001010
1111100000000000
1110100000000011
1101000000000000

Contributions - 
Prakhar Agrawal - 2022361 (prakhar22361@iiitd.ac.in)
Shobhit Raj - 2022482 (shobhit22482@iiitd.ac.in)
Souparno Ghose - 2022506 (souparno22506@iiitd.ac.in)
Sujal Soni - 2022513 (sujal22513@iiitd.ac.in)
