import abc
import enum


class ParamType(enum.Enum):
    POSITION = 'POSITION'
    IMMEDIATE = 'IMMEDIATE'


class Operation(object):

    def __init__(self, name, op_code, params_length, intcode):
        self.name = name
        self.op_code = op_code
        self.params_length = params_length
        self.params = []
        self.intcode = intcode

    @abc.abstractmethod
    def execute(self):
        raise NotImplementedError


class AddOp(Operation):

    def __init__(self, intcode):
        super().__init__('Add', 1, 3, intcode)

    def execute(self):
        print("Adding :{} {} to {}".format(self.params[0], self.params[1], self.params[2]))
        self.intcode.code[self.params[-1]] = self.intcode.code[self.params[0]] \
                                             + self.intcode.code[self.params[1]]


class MultOp(Operation):

    def __init__(self, intcode):
        super().__init__('Mult', 2, 3, intcode)

    def execute(self):
        print("Multing :{} {} to {}".format(self.params[0], self.params[1], self.params[2]))
        self.intcode.code[self.params[-1]] = self.intcode.code[self.params[0]] \
                                             * self.intcode.code[self.params[1]]


class HaltOp(Operation):

    def __init__(self, intcode=None):
        super().__init__('Halt', 99, 0, intcode)

    def execute(self):
        raise StopIteration


_operations = {
    1: AddOp,
    2: MultOp,
    99: HaltOp
}


class Parameter(object):

    def __init__(self, param_type, value):
        self.param_type = param_type
        self.value = value

    def find_value(self, code):
        if self.param_type == ParamType.POSITION:
            return code[self.value]
        elif self.param_type == ParamType.IMMEDIATE:
            return self.value
        raise ValueError("Invalid Value Param Type")


class IntCode(object):

    def __init__(self, code: list):
        self.code = code
        self.pc = 0

    def parse_op_code(self, op_code):
        pass

    def run(self):

        while True:
            op_code = self.code[self.pc]

            operation = _operations[op_code](self)

            for i in range(1, operation.params_length + 1):
                operation.params.append(self.code[self.pc + i])

            try:
                operation.execute()
            except StopIteration:
                print("Program Halted")
                break

            self.pc += operation.params_length + 1
