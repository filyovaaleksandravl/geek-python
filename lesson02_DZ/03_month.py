month_num = int(input("Введите номер месяца: "))
list_month = ["winter", "winter", "spring", "spring", "spring", "summer", "summer", "summer", "authomn", "authomn",
              "authomn", "winter"]
list_month_dicts = {1: "winter", 2: "winter", 3: "spring", 4: "spring", 5: "spring", 6: "summer", 7: "summer",
                    8: "summer", 9: "authomn", 10: "authomn",
                    11: "authomn", 12: "winter"}

print(f"Время года: {list_month[month_num - 1]}")
print(f"Время года: {list_month_dicts.get(month_num)}")