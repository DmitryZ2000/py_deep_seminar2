# Задание №6
# Напишите программу банкомат.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег

account = 0
counter_action = 0
MULTIPLICITY = 50
BONUS = 3 # Каждую третью операцию начисляем %
RICH_MAN = 5_000_000
WITHDRAWAL_FEE_PERCENT = 1.5
WITHDRAWAL_FEE_MIN = 30
WITHDRAWAL_FEE_MAX = 600

while True:
    action = input('Введите действие: пополнить, снять, выйти, набрав: deposit, withdraw, exit:  ')
    if action == 'deposit':
        while True:
            dep_number = int(input('Введите сумму пополнения кратную 50:  '))
            if not dep_number % MULTIPLICITY: # Проверяю на кратность 50
                break
        print(dep_number)
        
        if account > RICH_MAN:
            account *= 0.9 # Налог на богатства
        
        account += dep_number  # Само поплнение
        
        counter_action += 1
        print(account, counter_action)
        if counter_action % BONUS == 0: # Проверяю на кратность BONUS
            account *= (1+ BONUS/100)
            print(account)

    elif action == 'withdraw':
        while True:
            withdraw_number = int(input('Введите сумму снятия кратную 50:  '))
            if not withdraw_number % MULTIPLICITY: # Проверяю на кратность 50
                break
        if account > RICH_MAN:
            account *= 0.9 # Налог на богатства
        
        if withdraw_number > account:
            print('Недостаточно средств')
            break
        
        withdraw_fee =  withdraw_number * WITHDRAWAL_FEE_PERCENT / 100
        if withdraw_fee < WITHDRAWAL_FEE_MIN:
            account = account -  WITHDRAWAL_FEE_MIN - withdraw_number
        elif WITHDRAWAL_FEE_MIN < withdraw_fee < WITHDRAWAL_FEE_MAX:
            account = account - withdraw_fee - withdraw_number
        elif withdraw_fee > WITHDRAWAL_FEE_MAX:
            account = account -  WITHDRAWAL_FEE_MAX - withdraw_number
        
        counter_action += 1
        print(account, counter_action)
        if counter_action % BONUS == 0: # Проверяю на кратность BONUS
            account *= (1+ BONUS/100)
            print(account)
        

    elif action == 'exit':
        print(account)
        break







