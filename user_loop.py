from database.db_insert import insert_to_db
from database.db_select import DBManager

def user_loop():
    print('Привет! Добро пожаловать в мою программу.')
    while True:
        print('Доступные комманды:\n'
              '0 - Выход\n'
              '1 - Посмотреть интересующие компании с дальнейшей загрузкой в БД  <------- (Выбирай первым, т.к БД пуста. Данные берем ТОЛЬКО оттуда)\n'
              '2 - Получить список всех компаний и количество вакансий у каждой компании.\n'
              '3 - Получить список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.\n'
              '4 - Получить среднюю зарплату по всем вакансиям\n'
              '5 - Получить список всех вакансий, у которых зарплата выше средней по всем вакансиям.\n'
              '6 - Получить список всех вакансий, в названии которых содержатся переданные вами слова')

        command = input('Введите команду: ')
        print()

        if command == '0':
            print('Пока-пока!')
            DBManager('2344').close_connection()
            break

        if command == '1':
            insert_to_db()

        if command == '2':
            DBManager('2344').get_companies_and_vacancies_count()
            print('---------------')

        if command == '3':
            DBManager('2344').get_all_vacancies()
            print('---------------')

        if command == '4':
            print('Средняя зарплата: ')
            print(DBManager('2344').get_avg_salary())
            print('---------------')

        if command == '5':
            DBManager('2344').get_vacancies_with_higher_salary()
            print('---------------')

        if command == '6':
            word = input('Введите ключевое слово: ').capitalize()
            DBManager('2344').get_vacancies_with_keyword(word)
            print('---------------')
