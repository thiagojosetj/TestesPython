highest = 0
name = ""

while True:
    name, salary = input().split(', ')
    salary_int = float(salary)
    
    if name == "Fim": break

    if salary_int > highest:
        highest = salary_int
        
if highest != 0: print(f"{highest:.2f}")
else: print("Não tem")