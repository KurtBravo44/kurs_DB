import psycopg2

from api.hh_api_classes import HH_API
from api.get_vac import get_vac
from api.get_emp_vac import get_emp_vac

def run():
    user_answer = input('Ваша профессия: ')
    list_of_id_emp = get_vac(HH_API(user_answer).get_responce())
    vac_to_db = get_emp_vac(list_of_id_emp)
    return vac_to_db

def insert_to_db():

    vac_to_db = run()
    conn = psycopg2.connect(
        host='localhost',
        database='vacancies',
        user='postgres',
        password='2344'
    )
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute('SELECT * FROM employers')
                for emp in vac_to_db:
                    cur.execute('INSERT INTO employers VALUES (%s, %s) ON CONFLICT DO NOTHING',
                                (emp['employer']['id'], emp['employer']['name']))
                cur.execute('SELECT * FROM vacs')

                for vac in vac_to_db:
                    cur.execute('INSERT INTO vacs (title, company_id, salary_from, salary_to, url) VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING',
                                (vac['name'], vac['employer']['id'], vac['salary']['from'], vac['salary']['to'], vac['alternate_url']))

    finally:
        conn.close()

