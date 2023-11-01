
def get_vac(data):
    """Функция парсит вакансии, предоставляя информацию пользователю"""

    chosed_emp_id = []

    print('Список вакансий:')
    i = 0
    for vac in data:
        i += 1
        title = vac['name']
        company_name = vac['employer']['name']
        url = vac['alternate_url']
        payment_from = vac['salary']['from']
        payment_to = vac['salary']['to']
        if payment_from == None:
            payment_from = 'Не указана'
        if payment_to == None:
            payment_to = 'Не указана'

        print(f'{i}. {title}. Зарплата: от: {payment_from} до: {payment_to}. \n'
              f'Компания: {company_name}. \n'
              f' Ссылка на вакансию: {url}')
        print()
    print('0: Выход')
    print()
    while True:
        """Пользователь выбирает вакансии, после чего сохраняет его выбор"""

        command = input('Выберите компанию, которую хотите отследить: ')
        if command == '0':

            return chosed_emp_id
        else:
            if command.isdigit():
                number = int(command)
                if number > len(data):
                    print('Такой вакансии нет')
                else:
                    try:
                        chosed_emp_id.append(data[number - 1]['employer']['id'])
                    except:
                        print('У такой компании нет id')
            else:
                print('Введите номер вакансии')


