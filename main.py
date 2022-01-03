import math
import random

from art import logo

stack = []
operations = {}


def print_stack():
    for i in range(0, len(stack)):
        print(f"{i}: {stack[i]}")


# Operation functions starting  with oper_ are added automatically to the operations dictionary
# The key to use them is the string before , in the docstring

def oper_add():
    "+, add the top 2 elements"
    stack.append(stack.pop() + stack.pop())


def oper_subtract():
    "-, subtract the top 2 elements"
    stack.append(stack.pop() - stack.pop())


def oper_multiply():
    "*, multiply the top 2 elements"
    stack.append(stack.pop() * stack.pop())


def oper_divide():
    "-, divide the top 2 elements"
    stack.append(stack.pop() / stack.pop())


def oper_ceil():
    "ceil, ceil the top element"
    stack.append(math.ceil(stack.pop()))


def oper_clear():
    "clear, clear the stack"
    stack.clear()


def oper_drop():
    "drop, drop the top element"
    stack.pop()


def oper_pi():
    "pi, add pi to the stack"
    stack.append(random._pi)


def oper_stack_sum():
    "sum, add all elements of the stack"
    result = sum(stack)
    oper_clear()
    stack.append(result)


def oper_sort():
    "sort, sort all elements of the stack"
    stack.sort()


def oper_range():
    "range, add range of elements"
    for item in range(int(stack.pop()), int(stack.pop())):
        stack.append(item)


def oper_help():
    "?, show help"
    for fun in operations:
        print(operations[fun].__doc__)


print(logo)

for item in dir():
    if item.startswith("oper_"):
        try:
            myfun = locals()[item]
            info = myfun.__doc__
            ostring = info[:info.index(",")]
            operations[ostring] = myfun
        except:
            print(f"Error adding operation {item}")
    else:
        pass
        # print(f"{item} does not start with oper_")

"""
operations = { 
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
    "ceil":ceil,
    "clear":clear,
    "drop":drop,
    "sum":stack_sum,
}
"""
while True:
    print_stack()
    user_in = input("> ").lower()

    if user_in == "":
        break
    try:
        if user_in in operations:
            operations[user_in]()
        else:
            stack.append(float(user_in))
    except:
        print(f"Can't handle {user_in}")
        pass
