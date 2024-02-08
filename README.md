# chaithon
A new language having some components similar to Assembly interpreted in python, the language consists of 2 components- 1. Stack Memory: the complete code is revolving around a single stack upon which every command possible can be made, and 2.program memory, stored as tokens and traversed by a program counter that can either a)increment or b)jump if the top element in our stack is 0. I created this language in order to have a different approach towaards Computer Architecture and discover how to make it Turing complete even after having such a simple Architeture that I could simply create the Architecture in Hardware using ICs and Breadboards

to be able to run chaithon as one of my sample programs or create your own with ```.cy``` extension using simply cloning this repository using 

``` git clone https://github.com/chaitanyabatra/chaithon.git```

and going to the directory chaithon in your teminal and writing the following text

``` python3 chainterpreter.py [yourprogramname].cy```

I will try to create documentation for the same and keep updating this repository.
Thanks)


Documentation:

# Chaithon Language Interpreter Documentation

## Overview
This document serves as the official documentation for the custom language interpreter. The interpreter allows the execution of programs written in a custom programming language.

## Purpose
The custom language interpreter is designed to execute programs written in a custom programming language efficiently. It provides a set of instructions that can manipulate data on a stack and perform basic arithmetic operations. Additionally, it supports control flow instructions such as conditional jumps and printing. It is written to be low level and highly dependent on recursion, in order to give a deep understanding of it.

## Language Structure
The custom programming language supported by the interpreter follows a simple structure. Each line in the program consists of an opcode followed by optional operands separated by spaces.

### Opcodes
The interpreter recognizes the following opcodes:

- `PUSH <number>`: Pushes a number onto the stack.
- `POP`: Removes the top element from the stack.
- `ADD`: Adds the top two elements of the stack.
- `SUB`: Subtracts the top element from the second-to-top element on the stack.
- `PRINT "<string>"`: Prints a string literal.
- `READ`: Reads a number from the standard input and pushes it onto the stack.
- `JMPZ <label>`: Jumps to the specified label if the top element of the stack is zero.
- `TOP`: Prints the top element of the stack.
- `FKUP`: Randomly swaps the top two elements of the stack.
- `TWIN`: Duplicates the top element of the stack.
- `PUSHM`: Pushes the top element of the auxiliary memory onto the stack.
- `POPM`: Pops the top element of the stack and pushes it onto the auxiliary memory.
- `HALT`: Program memory traversal ends and you go back to terminal

### Comments
Comments can be included in the program by starting the line with a semicolon (`;`). Comments are ignored during program execution.

### Labels
Labels are used for defining points in the program that can be targeted by control flow instructions. Labels end with a colon (`:`) and must not have any spaces within them.

## Program Execution
The interpreter executes the program by sequentially interpreting each opcode and performing the corresponding operation. It maintains a stack for storing numerical values and supports basic arithmetic operations like addition and subtraction. Control flow instructions allow for conditional branching based on the stack's top element. Additionally, it provides functionality for printing strings, reading input, and manipulating the stack.

## Stack and Memory
The interpreter maintains two primary data structures:

### Stack
The stack is used to store numerical values and intermediate results during program execution. It supports operations such as pushing, popping, and accessing the top element.

### Auxiliary Memory
The auxiliary memory serves as a secondary storage space for preserving stack values during certain operations. It allows for temporary storage of data to facilitate more complex operations.

## Error Handling
Being a The interpreter provides minimal error handling. Errors such as invalid opcodes or incorrect program syntax may lead to undefined behavior or program termination.

## Usage
To use the custom language interpreter, follow these steps:

1. Write your program in the custom programming language, adhering to the syntax and structure described above.
2. Save your program in a text file with the appropriate file extension (`.cy`).
3. Run the interpreter with the path to your program file as a command-line argument.

Example:
```
python interpreter.py program.prog
```

## Contact
For questions, feedback, or bug reports, please contact [Chaitanya Batra](mailto:chaitanyabatra2003@gmail.com).

---

This documentation provides a comprehensive overview of the custom language interpreter, including its syntax, semantics, and usage instructions. Feel free to expand or customize it further based on your specific requirements.
