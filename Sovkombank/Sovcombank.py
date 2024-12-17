# Задача 1
cnt_shares = int(input('Введите число долей: '))
list_shares = [ float(input('Введите долю: ')) for _ in range(cnt_shares) ]

# сумма всех долей
sum_shares = sum(list_shares)

# получаем новый список уже с процентами
list_shares_rate = list (map(lambda x: round(x/sum_shares, 3), list_shares) )

print ('Процентное выражение долей:\n')
for elem in list_shares_rate:
    print('%.3f' % elem)
