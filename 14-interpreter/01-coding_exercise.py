# Interpreter Coding Exercise
# You are asked to write an expression processor for simple numeric expressions with the following constraints:
# Expressions use integral values (e.g., '13' ), single-letter variables defined in Variables, as well as + and - operators only
# There is no need to support braces or any other operations
# If a variable is not found in variables  (or if we encounter a variable with >1 letter, e.g. ab), the evaluator returns 0 (zero)
# In case of any parsing failure, evaluator returns 0
# Example:
# calculate("1+2+3")  should return 6
# calculate("1+2+xy")  should return 0
# calculate("10-2-x")  when x=3 is in variables  should return 5

from enum import Enum


class Token:
    class Type(Enum):
        INTEGER = 0
        MINUS = 1
        PLUS = 2
        VARIABLE = 3
    
    def __init__(self, type: Type, text: str) -> None:
        self.type = type
        self.text = text
    
    def __str__(self):
        return f'`{self.text}`'


class BinaryOp:
    class OpType(Enum):
        MINUS = 0
        PLUS = 1
    
    def __init__(self, type=None, left=None, right=None) -> None:
        self.left = left
        self.right = right
        self.type = type
        self.val = 0

    def update_val(self):
        if self.type == BinaryOp.OpType.MINUS:
            self.val = self.left - self.right
        elif self.type == BinaryOp.OpType.PLUS:
            self.val = self.left + self.right
        self.left = self.val
        self.right = None
    
    def update(self, int_value):
        if not self.left:
            self.left = int_value
        else:
            self.right = int_value
            self.update_val()


class ExpressionProcessor:
    def __init__(self):
        self.variables = {}
    
    def lex(self, expression: str) -> list[Token]:
        result = []
        i = 0
        while i < len(expression):
            if expression[i] == '+':
                result.append(Token(Token.Type.PLUS, expression[i]))
            elif expression[i] == '-':
                result.append(Token(Token.Type.MINUS, expression[i]))
            elif expression[i].isalpha():
                var_elems = [expression[i]]
                for j in range(i + 1, len(expression)):
                    if expression[j].isalpha():
                        var_elems.append(expression[j])
                        i += 1
                    else:
                        break
                var_name = str(''.join(var_elems))
                result.append(Token(Token.Type.VARIABLE, var_name))
                if var_name not in self.variables:
                    self.variables[var_name] = None
            else:
                integer_elems = [expression[i]]
                for j in range(i + 1, len(expression)):
                    if expression[j].isdigit():
                        integer_elems.append(expression[j])
                        i += 1
                    else:
                        break
                result.append(Token(Token.Type.INTEGER, str(''.join(integer_elems))))
            i += 1
        return result

    def parse(self, tokens: list[Token]) -> int:
        result = BinaryOp()
        i = 0

        while i < len(tokens):
            if tokens[i].type == Token.Type.INTEGER:
                result.update(int(tokens[i].text))
            elif tokens[i].type == Token.Type.VARIABLE:
                if not self.variables[tokens[i].text]:
                    return 0
                else:
                    result.update(self.variables[tokens[i].text])
            elif tokens[i].type == Token.Type.MINUS:
                result.type = BinaryOp.OpType.MINUS
            elif tokens[i].type == Token.Type.PLUS:
                result.type = BinaryOp.OpType.PLUS
            i += 1
        return result.val

    def calculate(self, expression):
        lex_tokens = self.lex(expression)
        print(' '.join(map(str, lex_tokens)))

        result = self.parse(lex_tokens)
        print(f'{expression} = {result}')
        
        return result


if __name__ == '__main__':
    ep = ExpressionProcessor()
    # ep.calculate("1+2+3")
    ep.variables['xy'] = 4
    ep.calculate("1+2+xy")
    ep.variables['x'] = 3
    ep.calculate("10-2-x")
    # eval('1+2+(3+4)')
    # eval('(13+4)-(12+1)')
    # eval('1+(3-4)')

    # this won't work
    # eval('1+2+(3-4)')