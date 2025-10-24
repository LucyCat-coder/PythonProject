salary = float(input("Укажите вашу заработную плату в месяц: "))
hypothec_percent = float(input("Укажите, какой процент(%) уходит на ипотеку: "))
life_percent = float(input("Укажите, какой процент(%) уходит на жизнь: "))
time_period = int(input("За какой временной отрезок в месяцах нужно рассчитать: "))
hypothec_money = (salary * hypothec_percent / 100) * time_period
life_money = (salary * life_percent / 100) * time_period
saved_money = salary * time_period - (hypothec_money + life_money)
print("На ипотеку было потрачено: ", hypothec_money)
print("На жизнь было потрачено: ", life_money)
print("Было накоплено: ", saved_money)