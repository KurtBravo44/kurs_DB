from api.hh_api_classes import HH_EMPLOYER

def get_emp_vac(index_list):
    """Функция получает вакансии компаний, идентификатор которых был выбран пользователем"""

    vac_list = []
    for i in index_list:
        for vacs in HH_EMPLOYER(i).get_responce():
            vac_list.append(vacs)
    return vac_list















