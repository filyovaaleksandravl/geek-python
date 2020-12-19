start_time = int(input("Введите время в секундах: "))
start_hours = start_time // 3600

start_minutes = start_time % 3600 // 60
start_seconds = start_time % 3600 % 60
if start_hours <= 9:
    start_hours = "0"+str(start_hours)
if start_minutes <= 9:
    start_minutes = "0"+str(start_minutes)
if start_seconds <= 9:
    start_seconds = "0"+str(start_seconds)
print(f"Корректный формат: {start_hours}:{start_minutes}:{start_seconds}")