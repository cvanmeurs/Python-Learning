# https://docs.python.org/3/reference/executionmodel.html
# A Python program is constructed from code blocks.
# A block is a piece of Python program text that is executed as a unit.
#
# The following are blocks: a module, a function body, and a class definition.

# A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended.
# https://docs.python.org/3/tutorial/modules.html

# Here is a function, whose body is its own block
def myFunction(foo, bar):
    print("This print statement is happening in the body of my function.")
    print("The body of this function is a block.")

# We have not covered classes yet, but understanding scope will be important when we do.
# Save this link for later:
# https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces

# Here is a class definition
class ComplexNumber:
    # This is the first line of the ComplexNumber scope
    def __init__(self, realPart, imaginaryPart):
        self.r = realPart
        self.i = imaginaryPart
    def toString(self):
        return f"{self.r} + {self.i}i"
    # This is the end of the ComplexNumber scope

# Here is an example of how this class can be used
x = ComplexNumber(3.0, -4.5)
print(f"x = {x.toString()}")

# A script file (a file given as standard input to the interpreter or specified as a command line argument to the interpreter) is a code block.
# A script command (a command specified on the interpreter command line with the -c option) is a code block.
# A module run as a top level script (as module __main__) from the command line using a -m argument is also a code block.
# The string argument passed to the built-in functions eval() and exec() is a code block.
