def sum_of(a, b):
    return a+b

def sub_of(a, b):
    return a-b

def mul_of(a, b):
    return a*b

def div_of(a, b):
    return a/b

def int_of_div(a, b):
    return a//b

def rem_of_div(a, b):
    return a%b

def inv_of(a, b):
    return a**b

op1 = 5
op2 = 6
print(f"sum of {op1} and {op2} is {sum_of(op1,op2)}")
print(f"sub of {op1} and {op2} is {sub_of(op1,op2)}")
print(f"mul of {op1} and {op2} is {mul_of(op1,op2)}")
print(f"div of {op1} and {op2} is {div_of(op1,op2)}")
print(f"int of div {op1} and {op2} is {int_of_div(op1,op2)}")
print(f"rem of div {op1} and {op2} is {rem_of_div(op1,op2)}")
print(f"inv of {op1} and {op2} is {inv_of(op1,op2)}")