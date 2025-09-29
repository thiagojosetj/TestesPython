lowest = None
name_lowest = ""

while True:
    name, salary = input().split(',')
    salary_int = float(salary)
    
    if name == "Fim": break

    if lowest is None or salary_int < lowest:
        lowest = salary_int
        name_lowest = name

if lowest is not None: print(name_lowest)
else: print("Não tem")