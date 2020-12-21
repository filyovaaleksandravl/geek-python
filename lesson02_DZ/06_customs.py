Data_base = [
    (1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
    (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
    (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})
]

name = []
cost = []
amount = []
items = []

for i, dicts in Data_base:
    name.append(dicts.get("название"))
    cost.append(dicts.get("цена"))
    amount.append(dicts.get("количество"))
    items.append(dicts.get("eд"))
new_items = set(items)
new_dicts = {"название": name, "цена": cost, "количество": amount, "eд": new_items}

while True:
    ask_question = input("Напишите интересующий параметр (название, цена, количество, ед): ")
    print(new_dicts.get(ask_question))
    break
