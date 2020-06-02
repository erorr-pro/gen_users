import random
import csv

import man_name
import woman_name
import mail_coll

from random import randint


######################### ПЛАНИРУЕМЫЙ ФУНКЦИОНАЛ ###################################
# print('Данный скрипт генерирует юзеров для нагрузочного тестирования. Он способен генерировать ФИО (как цельной '
#       'записью, так и раздельно), логин, почту и пароль. Создаётся файл CSV.')
# print('\nВведите "FIO" чтобы сгенерировать "ФИО" в одну строку')
# print('Введите "F" чтобы сгенерировать "Фамилию" отдельно')
# print('Введите "I" чтобы сгенерировать "Имя" отдельно')
# print('Введите "O" чтобы сгенерировать "Отчество" отдельно')
# print('Введите "L" чтобы сгенерировать "login"')
# print('Введите "E" чтобы сгенерировать "e-mail"')
# print('Введите "P" чтобы сгенерировать "password"')
#
# print('\nЧерез запятую укажите юзеры с какими данными Вам нужны.')
# config = str(input())

######################### ВВОДНЫЕ ДАННЫЕ ###################################
print('\nСколько нужно пользователей? (один или более, для уникальности ФИО рекомендуется не больше 1000)')
the_users = int(input())

print('Из скольки символов должен состоять никнейм? (от 5-х до 20-ти символов)')
the_nick = int(input()) - int(3)

print('Длина пароля? (от 8-ми до 30-ти символов)')
the_pass = int(input())

############################ ГЕНЕРИРУЕМ ФИО #############################
data_fio = []
for fio in range(the_users):
    random_gender = randint(0, 1)
    if random_gender == 0:
        data_fio.append(random.choice(woman_name.w_family) + ' ' + random.choice(woman_name.w_name) + ' ' +
                        random.choice(woman_name.w_patronymic))
    else:
        data_fio.append(random.choice(man_name.m_family) + ' ' + random.choice(man_name.m_name) + ' ' +
                        random.choice(man_name.m_patronymic))
print(data_fio)

############################ ГЕНЕРИРУЕМ НИКНЭЙМЫ #############################

symbols_nick = 'aaaaabcdeeefghiijklmnoooopqrstuvwxyz'
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

data_nickname = []
for nick_wd in range(the_users):
    list_symbols_nick = list(symbols_nick)  # Преобразуем в посимвольный список
    random.shuffle(list_symbols_nick)  # Перемешиваем символы в посимвольном списке
    symbols_random = ''.join(list_symbols_nick[0:the_nick])  # Преобразуем перемешанные символы в строку, берём первые n
    data_nickname.append(symbols_random)
# print(data_nickname_full)

prefix_nom = []
for number_name in range(the_users):
    prefix_nom.append(random.choice(numbers) + random.choice(numbers) + random.choice(numbers) + random.choice(numbers))
# print(prefix_nom)

data_nickname_full = []
for i in range(0, len(data_nickname)):
    data_nickname_full.append(data_nickname[i] + prefix_nom[i])
print(data_nickname_full)

############################ ГЕНЕРИРУЕМ E-MAIL #############################
random_email_list = []

for nm in range(the_users):
    random_email_list.append(random.choice(mail_coll.random_email))
# print(random_email_list)


email = []

for em in range(0, len(random_email_list)):
    email.append(str(data_nickname_full[em]) + random.choice(mail_coll.random_email))
print(email)

############################ ГЕНЕРИРУЕМ ПАРОЛИ #############################
pass_symbols = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
pass_list = []

for pass_wd in range(the_users):
    pass_symbols_list = list(pass_symbols)  # Преобразуем в посимвольный список2000
    random.shuffle(pass_symbols_list)  # Перемешиваем символы в посимвольном списке
    list_symbols_random = ''.join(
        pass_symbols_list[0:the_pass])  # Преобразуем перемешанные символы в строку, берём первые 14
    pass_list.append(list_symbols_random)
print(pass_list)

############################ ЗАПИСЬ В CSV #############################

data = zip(data_fio, data_nickname_full, email, pass_list)

with open('fio_data_new.csv', mode='w', encoding='utf-16', newline='') as f:  # encoding='utf-16'
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)

############################ ОБРАТНАЯ СВЯЗЬ ##################################
setarr_data_nickname_full = set(data_nickname_full)
if len(data_nickname_full) == len(setarr_data_nickname_full):
    print("Успех! Никнеймы уникальны!")
else:
    print("Есть одинаковые никнеймы клиентов! Рекомендуестя сгенерировать новый файл увеличив длину никнейма!")

setarr_data_fio = set(data_fio)
if len(data_fio) == len(setarr_data_fio):
    print("Успех! ФИО уникальны!")
else:
    print(
        "Есть одинаковые ФИО клиентов! Рекомендуестя уменьшить количество пользователей или сгенерировать новый файл!")
