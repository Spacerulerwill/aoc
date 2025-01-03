import re
from dataclasses import dataclass, field
from typing import Any

ADV = 0
BXL = 1
BST = 2
JNZ = 3
BXC = 4
OUT = 5
BDV = 6
CDV = 7


@dataclass
class Interpreter:
    a: int
    b: int
    c: int
    pc: int = 0
    out: list[int] = field(default_factory=list)

    def get_value_of_combo_operand(self, operand: int) -> int:
        if 0 <= operand <= 3:
            return operand
        elif operand == 4:
            return self.a
        elif operand == 5:
            return self.b
        elif operand == 6:
            return self.c
        elif operand == 7:
            raise ValueError("Seven in program")
        raise ValueError("WTF?")

    def interpret_opcode(self, opcode: int, operand: int) -> None:
        if opcode == ADV:
            self.a //= 2 ** self.get_value_of_combo_operand(operand)
            self.pc += 2
        elif opcode == BXL:
            self.b ^= operand
            self.pc += 2
        elif opcode == BST:
            self.b = self.get_value_of_combo_operand(operand) % 8
            self.pc += 2
        elif opcode == JNZ:
            if self.a == 0:
                self.pc += 2
            else:
                self.pc = operand
        elif opcode == BXC:
            self.b ^= self.c
            self.pc += 2
        elif opcode == OUT:
            self.out.append(self.get_value_of_combo_operand(operand) % 8)
            self.pc += 2
        elif opcode == BDV:
            self.b = self.a // (2 ** self.get_value_of_combo_operand(operand))
            self.pc += 2
        elif opcode == CDV:
            self.c = self.a // (2 ** self.get_value_of_combo_operand(operand))
            self.pc += 2

    def run_program(self, program: list[int]) -> None:
        while self.pc < len(program):
            opcode = program[self.pc]
            operand = program[self.pc + 1]
            self.interpret_opcode(opcode, operand)


def puzzle(input: str) -> Any:
    matches = re.search(
        r"""Register A: (\d+)
Register B: (\d+)
Register C: (\d+)

Program: ((?:\d+,)*\d+)""",
        input,
    )

    if matches is None:
        raise ValueError("Invalid input")

    a = int(matches.group(1))
    b = int(matches.group(2))
    c = int(matches.group(3))
    program = [int(num) for num in matches.group(4).split(",")]

    interpreter = Interpreter(a, b, c)
    interpreter.run_program(program)
    return ",".join(str(num) for num in interpreter.out)
