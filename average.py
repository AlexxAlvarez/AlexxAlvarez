import math

# Defino la probabilidad ρ y el promedio P
rho = 0.37
P = 0

# Calcular el promedio P
for i in range(0,26):  # de 0 a 26
    Pr_i = (rho ** i)*(1-rho)  # Probabilidad de i
    n = 2*math.ceil(math.log2(i+2))-1
    print(n)
    P = P + Pr_i*n

# Imprimo el promedio
print(f"El promedio P del número de bits por carácter del alfabeto es: {P:.4f}")
