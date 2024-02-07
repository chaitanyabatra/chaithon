import sys
import random

program_filepath = sys.argv[1]

#
#
#
#Tokenizing the program
#
#
#


program_lines=[]

with open(program_filepath,"r") as program_file:
    program_lines=[
        line.strip() for line in program_file.readlines()
    ]
    
program=[]
token_counter = 0
label_tracker = {}
for line in program_lines:
    parts  = line.split(" ")
    opcode = parts[0]
    
    if opcode=="":
        continue #ignore blank line

    if opcode.startswith(";"):
        continue #treat as comment
    
    if opcode.endswith(":"):
        label_tracker[opcode[:-1]]=token_counter
        continue #loop / label creating a map with their index
    
    program.append(opcode)
    token_counter+=1
    
    if opcode == "PUSH":
        # expecting a number
        number = int(parts[1])
        program.append(number)
        token_counter += 1
    elif opcode == "PRINT":
        # parse string literal
        string_literal = ' '.join(parts[1:])[1:-1]
        program.append(string_literal)
        token_counter += 1
    elif opcode == "JMPZ":
        # read label
        label = parts[1]
        program.append(label)
        token_counter += 1

#
#
#
#
#        
#     Interpret Program
#
#
#
#
#


class Stack:

    def __init__(self, size):
        self.buf = [0 for _ in range(size)]
        self.sp    = -1

    def push(self, number):
        self.sp += 1
        self.buf[self.sp] = number
    
    def pop(self):
        number = self.buf[self.sp]
        self.sp -= 1
        return number
    
    def top(self):
        return self.buf[self.sp]
    
    
pc = 0
stack = Stack(256)
print(program)

while program[pc] != "HALT":
    opcode=program[pc]
    pc+=1
    
    
    if opcode == "PUSH":
        number = program[pc]
        pc += 1

        stack.push(number)
    elif opcode == "POP":
        stack.pop()
    elif opcode == "ADD":
        a = stack.pop()
        b = stack.pop()
        stack.push(a+b)
    elif opcode == "SUB":
        a = stack.pop()
        b = stack.pop()
        stack.push(b-a)
    elif opcode == "PRINT":
        string_literal = program[pc]
        pc += 1
        print(string_literal)
    elif opcode == "READ":
        number = int(input())
        stack.push(number)
    elif opcode == "JMPZ":
        number = stack.top()
        if number == 0:
            pc = label_tracker[program[pc]]
        else:
            pc += 1
            
    elif opcode == "TOP":
        print(stack.top())
        
    elif opcode == "FKUP":
        randint = random.randrange(0,2)
        if(randint==0):
            a = stack.pop()
            b = stack.pop()
            stack.push(a)
            stack.push(b)
    elif opcode == "TWIN":
        stack.push(stack.top())
    
        
        