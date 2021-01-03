with open('03_file_file', 'r', encoding='utf-8') as my_file:
    wokers = {}
    wokers_amount = 0
    sum_salary = 0
    for woker in my_file:
        last_name, salary = woker.split()
        wokers[last_name] = salary
        wokers_amount += 1
        sum_salary = sum_salary + float(salary)

        if float(salary) < 20000:
            print(f"{last_name}: зарплата меньше 20000")
print(f"{sum_salary / wokers_amount} - средний доход сотрудников")
