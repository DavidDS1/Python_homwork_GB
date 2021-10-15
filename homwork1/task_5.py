#задание 5
proceeds = int(input('Введите месчную выручку вашей компании: '))
costs = int(input('Введите месячные расходы вашей компании: '))
if proceeds>costs:
    profit = proceeds-costs
    profitability = (profit/proceeds)*100
    profitability=round(profitability,1)
    print(f'Прибыль компании составляет {profit}')
    print(f'Рентабельность компании составляет {profitability}%')
else:
    damages = costs-proceeds
    print(f'Ваша компания убыточная. Убыток составляет {damages}')
