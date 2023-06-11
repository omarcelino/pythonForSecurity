from mod1 import Calculator
from packagedemo.Calculator import Calculator
from packagedemo.AdvancedCalc import AdvancedCalc

calc = Calculator(4,5)
advcal = AdvancedCalc(3,6)

print(calc.add())
print(advcal.power())