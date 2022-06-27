money = float(input('money='))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = list(map(int,list(map(lambda x: x*money/100, per_cent.values()))))
print('Возможные накопленные средства за год вклада в каждом из банков', deposit)
print('Максимальная сумма, которую вы можете заработать', max(deposit))
