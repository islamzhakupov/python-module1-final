print("Программа «Накопления на покупку»")

MONTHS = 6

def get_status(saved, cost):
    if saved < cost:
        return "Цель пока не достигнута"
    elif saved == cost:
        return "Цель достигнута"
    else:
        return "Цель достигнута с остатком"

def print_month_table(initial, monthly, cost):
    print()
    print(f"{'Месяц':<8}{'Накопленная сумма':>20}{'Процент от стоимости':>24}")
    print("-" * 60)
    saved = initial
    for month in range(1, MONTHS + 1):
        saved += monthly
        percent = saved / cost * 100
        print(f"{month:<8}{saved:>20.2f}{percent:>23.1f}%")
    return saved

def print_report(name, cost, initial, monthly):
    print(f"Название покупки: {name}")
    print(f"Стоимость покупки: {cost:.2f}")
    print(f"Первоначальные накопления: {initial:.2f}")
    print(f"Ежемесячный взнос: {monthly:.2f}")
    print(f"Период прогноза: {MONTHS} мес.")

    final_sum = print_month_table(initial, monthly, cost)
    share = final_sum / cost * 100
    status = get_status(final_sum, cost)

    print()
    print(f"{'Стоимость покупки:':<40}{cost:>20.2f}")
    print(f"{'Сумма после 6 месяцев:':<40}{final_sum:>20.2f}")
    print(f"{'Доля от стоимости:':<40}{share:>19.1f}%")

    if final_sum < cost:
        print(f"{'Недостающая сумма:':<40}{cost - final_sum:>20.2f}")
    else:
        print(f"{'Остаток:':<40}{final_sum - cost:>20.2f}")

    print(f"{'Статус:':<40}{status:>20}")
    return final_sum

def ask_again():
    while True:
        answer = input("\nРассчитать накопления на другую покупку? (да/нет): ").strip().lower()
        if answer == "да":
            return True
        if answer == "нет":
            return False
        print("Пожалуйста, введите «да» или «нет».")


while True:
    name = input("Введите название товара: ")
    price = float(input("Введите цену товара: "))
    start_money = float(input("Введите начальную сумму денег: "))
    each_month = float(input("Введите ежемесячный доход: "))

    while price <= 0:
        print("Ошибка: цена должна быть положительной.")
        price = float(input("Введите цену товара: "))

    while each_month <= 0:
        print("Ошибка: ежемесячный доход должен быть положительным.")
        each_month = float(input("Введите ежемесячный доход: "))

    while start_money < 0 or start_money > price:
        print("Ошибка: начальная сумма должна быть неотрицательной и не больше стоимости покупки.")
        start_money = float(input("Введите начальную сумму денег: "))

    print_report(name, price, start_money, each_month)

    if not ask_again():
        print("Работа программы завершена")
        break