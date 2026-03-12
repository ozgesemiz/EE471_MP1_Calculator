from custom_classes import Calculator

calc = Calculator()

result = calc.divide(calc.multiply(calc.add(10, 5), 2), 3)
print(result)