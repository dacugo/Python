i = 0
while i < 100:
    # hacer_algo()
    i += 1 
"""
 for i in range (100):
    #hacer algo()
    pass

for i in range(10):
    print("El valor de i es actualmente", i)
"""
for i in range (2, 8):
    print("El valor de i es actualmente", i)

for i in range(2, 8, 3):
    print("El valor de i es actualmente", i)

# break - ejemplo

print("La instrucción de ruptura:")
for i in range(1,6):
    if i == 3:
        break
    print("Dentro del ciclo.", i)
print("Fuera del ciclo.")

# continua - ejemplo

print("\nLa instrucción continue:")
for i in range(1,6):
    if i == 3:
        continue
    print("Dentro del ciclo.", i)
print("Fuera del ciclo.")