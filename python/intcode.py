class computer:
    OPCODES = {
            1: (2, lambda x, y: x + y),
            2: (2, lambda x, y: x * y)
    }
    def __init__(self, memory):
        self.memory = memory
        self.instruction_pointer = 0
        self.terminate = False

    def process_opcode(self):
        mem = self.memory.copy()
        ip = self.instruction_pointer

        opcode = mem[self.instruction_pointer]
        if opcode == 99:
            self.terminate = True
            return

        num_arguments, f = self.OPCODES[opcode]
        arg_pointers = mem[ip+1:ip+num_arguments+1]
        arguments = [mem[x] for x in arg_pointers]

        output_pointer = mem[self.instruction_pointer + num_arguments + 1]

        mem[output_pointer] = f(*arguments)

        self.memory = mem
        self.instruction_pointer += 4

    def run(self):
        while not self.terminate:
            self.process_opcode()
