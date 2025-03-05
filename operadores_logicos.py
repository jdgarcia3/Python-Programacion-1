num1 = 5
num2 = 5
num3 = 10

#OL: Operador Lógico
#OL: and - multiplicación lógica (&)
print(num1 == num2 and num1 != num3)# 1 1 = 1
print(num1 == num2 and num1 > num3)# 1 0 = 0
print(num1 != num2 and num1 > num3)# 0 0 = 0
print(num1 != num2 and num1 < num3)# 0 1 = 0

#OL: or - suma lógica (|)
print(num1 == num2 or num1 != num3)# 1 1 = 1
print(num1 == num2 or num1 > num3)# 1 0 = 1
print(num1 != num2 or num1 > num3)# 0 0 = 0
print(num1 != num2 or num1 < num3)# 0 1 = 1

#OL: not - inversor lógico
print(not num1 == num2)# 1 = 0
print(not num1 != num2)# 0 = 1

