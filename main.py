import random
import math


#all the operations
def add(number1,number2):
  x = number1 + number2
  return x


def sub(number1,number2):
  y = number1 - number2
  return y


def mult(number1,number2):
  z = number1 * number2
  return z

def div(number1,number2):
  q = number1 / number2
  return q


#the inputs
number1 = float(input('whats your first number  '))
number2 = float(input('whats the second  '))

text = input('Add      Sub      Mult      Div   :  ') 

#Addition
if text == 'add' or text == 'Add' or text == 'addition' or text == 'Addition' or text == '+':
  a = add(number1,number2)
  print('Result: ', a)

#Subtraction
elif text == 'sub'or text == 'Sub' or text == 'Subtraction' or text == 'subtraction' or text == '-' or text == 'subtract' or text == 'Subtract':
  s = sub(number1,number2)
  print('Result: ', s)

#Multiplication
elif text == 'mult' or text == 'multiply' or text == '*' or text == 'x' or text == 'Multiply' or text == 'multiplication' or text == 'Multiplication':
  m = mult(number1,number2)
  print('Result:  ', m)

#Division
elif text == 'Division' or text == 'division' or text == 'Divide' or text == 'divide' or text == 'div' or text == 'Div' or text == '/':
  d = div(number1,number2)
  print('Result  ', d)
  