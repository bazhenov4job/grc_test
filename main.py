"""Сделать маленький вариант базы данных. Никакого сетевого
взаимодействия не нужно. данные читаются из stdin.
База лежит в оперативной памяти. Одна строка, всегда ровно один запрос. Аргументы
команд пробелов не содержат. Также в вводе должен рапозноваться EOF,
который означает конец ввода и завершение приложения."""


data_base = {}
command = ''
is_transaction = False

while command != 'END':

    command = input('')

    if command.startswith('SET'):

        variable = command[command.find(' ') + 1: command.rfind(' ')]
        value = [command[command.rfind(' ') + 1:]]
        if is_transaction:
            data_base[variable].append(value[0])
        else:
            data_base[variable] = value
        print(data_base)

    if command.startswith('GET'):
        variable = command[command.find(' ') + 1:]
        try:
            data_base[variable]
        except KeyError:
            print('No such value in db...')

        if is_transaction:
            print(data_base[variable][-1])
        else:
            print(data_base[variable][0])

    if command.startswith('UNSET'):
        variable = command[command.find(' ') + 1:]
        if variable in data_base.keys():
            del data_base[variable]
        print(data_base)

    if command.startswith('COUNTS'):
        value = command[command.find(' ') + 1:]
        count = 0
        for each_value in data_base.values():
            if each_value[0] == value:
                count += 1
        print(count)

    if command.startswith('BEGIN'):
        is_transaction = True

    if command.startswith('ROLLBACK'):
        for key, value in data_base.items():
            data_base[key] = [data_base[key][0]]

    if command.startswith('COMMIT'):
        for key, value in data_base.items():
            data_base[key] = [data_base[key][-1]]
        is_transaction = False


