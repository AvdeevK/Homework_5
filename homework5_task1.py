# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно
# вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.


from collections import defaultdict, namedtuple


num = int(input('Введите количество компаний: '))

companies = defaultdict(list)

for i in range(num):
    summator = 0

    name = input('Введите название компании: ')
    companies['Наименование компании'].append(name)

    frst_q = int(input('Введите доход за первый квартал: '))
    companies['Первый квартал'].append(frst_q)
    summator += frst_q

    scnd_q = int(input('Введите доход за второй квартал: '))
    companies['Второй квартал'].append(scnd_q)
    summator += scnd_q

    thrd_q = int(input('Введите доход за третий квартал: '))
    companies['Третий квартал'].append(thrd_q)
    summator += thrd_q

    frth_q = int(input('Введите доход за четвертый квартал: '))
    companies['Четвертый квартал'].append(frth_q)
    summator += frth_q

    companies['Доход за год'].append(summator)  # По этому ключу хранится общий доход каждой компании

overage = sum(companies['Доход за год']) / num

idx_positive = 0
for income in companies['Доход за год']:
    if income > overage:
        for key, value in companies.items():
            print(f'{key}: {value[idx_positive]}')
    idx_positive += 1

print('************************ Компании с доходом ниже среднего *******************************')


idx_negative = 0
for income in companies['Доход за год']:
    if income < overage:
        for key, value in companies.items():
            print(f'{key}: {value[idx_negative]}')
    idx_negative += 1


############################################ Второй вариант решения ####################################################


company = namedtuple('Company', ['Name', 'First', 'Second', 'Third', 'Fourth', 'Summa'])
number = int(input('Введите количество компаний: '))
all_comp = []
summa = 0
for i in range(number):
    name = input('Введите название компании: ')
    frst = int(input('Введите доход за первый квартал: '))
    summa += frst

    scnd = int(input('Введите доход за второй квартал: '))
    summa += scnd

    thrd = int(input('Введите доход за третий квартал: '))
    summa += thrd

    frth = int(input('Введите доход за четвертый квартал: '))
    summa += frth

    all_comp.append(company(name, frst, scnd, thrd, frth, summa))

common = 0
for i in range(len(all_comp)):
    common += all_comp[i].Summa

overage = common/number

for j in range(len(all_comp)):
    if all_comp[j].Summa > overage:
        print(all_comp[j])

print('******************************** Компании с низким доходом *********************************')

for k in range(len(all_comp)):
    if all_comp[k].Summa < overage:
        print(all_comp[k])