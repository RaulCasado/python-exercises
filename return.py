def factorizar_primos(num):
    factores = []
    divisor = 2
    while num > 1:
        while num % divisor == 0:
            factores.append(divisor)
            num = num / divisor
        divisor += 1
    return factores

print(factorizar_primos(56))

