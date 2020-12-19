proceeds_ = int(input("Введите значение выручки в руб.: "))
costs_ = int(input("Введите значение издержек в руб.: "))
if proceeds_ > costs_:
    print(f"Фирма отработала с прибылью. Рентабельность: {proceeds_/costs_}")
    number_of_coworkers = int(input("Введите количество сотрудников: "))
    print(f"Прибыль фирмы в расчете на одного сотрудника: {proceeds_ - costs_/ number_of_coworkers}")
elif proceeds_<costs_:
    print("Фирма отработала в убыток")
