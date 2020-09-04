def saludar(nombre):
    return("Hola {} ").format(nombre)

def SalaryWeek(hrs, salaryHr, Job):
    salary = hrs * salaryHr
    salary = salary * 7
    print ("El salario del ", Job, " es: ",salary)
print("Ingresa tu nombre")
nombre = input()
print(saludar(nombre))
SalaryWeek(8,284,"Doctor")