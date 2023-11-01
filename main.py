from database.db_insert import insert_to_db
from database.db_select import DBManager



def main():
#    insert_to_db()
    p = DBManager
    DBManager.get_companies_and_vacancies_count(p)


if __name__ == '__main__':
    main()