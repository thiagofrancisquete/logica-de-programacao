n = 1
soma = 0
while n <= 10:
    x = int(input("digite o %d numero: " %n))
    soma = soma + x
    n = n + 1
print("media: %5.2f" %(soma/10))
