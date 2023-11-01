import psycopg2

class DBManager:
    """Получение информации из БД"""
    def __init__(self, password):
        self.conn = psycopg2.connect(
            host='localhost',
            database='vacancies',
            user='postgres',
            password=password
        )
        self.cur = self.conn.cursor()

    def get_companies_and_vacancies_count(self):
        self.cur.execute("SELECT company_name, COUNT(*)"
                         " FROM employers JOIN vacs USING(company_id)"
                         " GROUP BY company_name")
        rows = self.cur.fetchall()
        print('Компании:')
        for i, row in enumerate(rows):
            print(f'{i+1}. {row[0]}.\n'
                  f'Количество вакансий:{row[1]}')

    def get_all_vacancies(self):
        self.cur.execute('SELECT title, salary_from, salary_to, url, employers.company_name FROM vacs'
                         ' JOIN employers USING(company_id)')
        rows = self.cur.fetchall()
        print("Вакансии: ")
        for i, row in enumerate(rows):
            print(f'{i+1}. {row[4]}. "{row[0]}"\n'
                  f'Зарплата от: {row[1]}, до: {row[2]}. Ссылка: {row[3]}')
            print('_________')

    def get_avg_salary(self):
        self.cur.execute('SELECT AVG((salary_to + salary_from) / 2) FROM vacs')
        rows = self.cur.fetchall()
        return round(int(rows[0][0]))

    def get_vacancies_with_higher_salary(self):
        self.cur.execute(f'SELECT title, (COALESCE(salary_from, 0) + COALESCE(salary_to, 0)) / 2, employers.company_name FROM vacs'
                         f' JOIN employers USING(company_id)'
                         f' WHERE  (COALESCE(salary_from, 0) + COALESCE(salary_to, 0)) / 2 > {self.get_avg_salary()}')
        rows = self.cur.fetchall()
        for i, vac in enumerate(rows):
            print(f'{i+1}. {vac[2]}, Средняя ЗП: {vac[1]}\n'
                  f' {vac[0]}')

    def get_vacancies_with_keyword(self, word):
        self.cur.execute(f"SELECT title, salary_from, salary_to, url FROM vacs WHERE title LIKE '{word}%'")
        rows = self.cur.fetchall()
        print("Вакансии: ")
        for i, vac in enumerate(rows):
            print(f'{i+1}. {vac[0]}. Запралата: От {vac[1]}, До {vac[2]}\n'
                  f'Ссылка: {vac[3]}')

    def close_connection(self):
        self.conn.close()
        self.cur.close()




