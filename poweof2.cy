BOOTLOADER:
PUSH 2
READ
PUSH 1
SUB
POPM
PUSH 0
JMPZ CHECK
HALT

CHECK:
POP
PUSHM
JMPZ PRINT
PUSH 0
JMPZ MUL
HALT

PRINT:
POP
TOP
HALT

MUL:
POP
PUSH 1
SUB
POPM
TWIN
ADD
PUSH 0
JMPZ CHECK
HALT
