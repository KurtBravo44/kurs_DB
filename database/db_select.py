import psycopg2

class DBManager:
    def __init__(self):
        self.conn = psycopg2.connect(
            host='localhost',
            database='vacancies',
            user='postgres',
            password='2344'
        )
        self.cur = self.conn.cursor()

    def close_connection(self):
        self.conn.close()
        self.cur.close()

    def get_companies_and_vacancies_count(self):
        self.cur.execute("SELECT * FROM vacs")
        rows = self.cur.fetchall()
        for row in rows:
            print(row)




