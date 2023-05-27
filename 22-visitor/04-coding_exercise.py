# Visitor Coding Exercise
# You are asked to implement a visitor called ExpressionPrinter
# for printing different mathematical expressions.
# The range of expressions covers addition and multiplication - please put round brackets around addition operations
# (but not multiplication ones)! Also, please avoid any blank spaces in output.
# Example:
# Input: AdditionExpression(Value(2), Value(3)) 
# Output: (2+3)


def _qualname(obj):
    """Get the fully-qualified name of an object (including module)."""
    return obj.__module__ + '.' + obj.__qualname__


def _declaring_class(obj):
    """Get the name of the class that declared an object."""
    name = _qualname(obj)
    return name[:name.rfind('.')]


# Stores the actual visitor methods
_methods = {}


# Delegating visitor implementation
def _visitor_impl(self, arg):
    """Actual visitor method implementation."""
    key = (_qualname(type(self)), type(arg))
    if not key in _methods:
        raise Exception('Key % not found' % key)
    method = _methods[key]
    return method(self, arg)


# The actual @visitor decorator
def visitor(arg_type):
    """Decorator that creates a visitor method."""

    def decorator(fn):
        declaring_class = _declaring_class(fn)
        _methods[(declaring_class, arg_type)] = fn

        # Replace all decorated methods with _visitor_impl
        return _visitor_impl

    return decorator

# ↑↑↑ LIBRARY CODE ↑↑↑


class Value:
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        visitor.visit(self)


class AdditionExpression:
    def __init__(self, left: Value, right: Value):
        self.right = right
        self.left = left
    
    def accept(self, visitor):
        visitor.visit(self)


class MultiplicationExpression:
    def __init__(self, left, right):
        self.right = right
        self.left = left

    def accept(self, visitor):
        visitor.visit(self)


class ExpressionPrinter:
    def __init__(self):
        self.buffer = []

    @visitor(Value)
    def visit(self, val: Value):
        self.buffer.append(str(val.value))

    @visitor(AdditionExpression)
    def visit(self, ae: AdditionExpression):
        self.buffer.append('(')
        ae.left.accept(self)
        self.buffer.append('+')
        ae.right.accept(self)
        self.buffer.append(')')
        
    @visitor(MultiplicationExpression)
    def visit(self, me: MultiplicationExpression):
        me.left.accept(self)
        self.buffer.append('*')
        me.right.accept(self)

    def __str__(self):
        return ''.join(self.buffer)


if __name__ == "__main__":
    # simple = AdditionExpression(Value(2), Value(3))
    # ep = ExpressionPrinter()
    # ep.visit(simple)
    # assert ("(2+3)" == str(ep))

    simple = MultiplicationExpression(
                AdditionExpression(Value(2), Value(3)), 
                Value(4)
            )
    ep = ExpressionPrinter()
    ep.visit(simple)
    assert ("(2+3)*4" == str(ep))

    # (2+3)*4