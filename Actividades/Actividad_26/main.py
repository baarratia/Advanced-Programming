import requests
import json
from classes import ConsoleApp, Student

__author__ = 'Patricio Lopez'


class SpyKiller:
    def __init__(self, my_name, my_username, url):
        self.my_username = my_username
        self.my_name = my_name
        self.url = url

    def mark_unassistent(self, victim):
        """
        Marca como inasistente a un estudiante, recibiendo su objeto Student.
        La peticion al servidor debe declarar 'assistance' y su valor booleano.
        """

        request = None
        a = 'http://assistance-py.herokuapp.com/students/'+ str(victim.id)
        r = requests.patch(url= a,params={'assistance': False})
        print(r)

        if request and request.status_code == 202:
            return "Devuelve el JSON de la response si fue exitosa"
        return "Devuelve un mensaje de error"

    def register_me(self):
        """
        Registra tu usuario en el servidor
        """
        username = self.my_username
        name = self.my_name
        assistance = True

        request = None
        r = requests.post('http://assistance-py.herokuapp.com/students',
                          params={'name': name, 'username': username, 'assistance': assistance})
        print(r)

        if request and request.status_code == 201:
            return "Devuelve el JSON de la response si fue exitosa"
        return "Devuelve un mensaje de error"

    def download_list(self):
        """
        Devuelve una lista de Student con todos los estudiantes en el servidor
        """

        students = []

        r = requests.get('http://assistance-py.herokuapp.com/students')
        dic = dict(json.loads(r.text))
        print((dic['students']))
        for i in dic['students']:
            id = i['id']
            name = i['name']
            username = i['username']
            assistance = i['assistance']
            students.append(Student(id, name, username, assistance))

        return students


if __name__ == "__main__":
    # CUIDADO! USERNAME ES CASE SENSITIVE! REVISE EL ARCHIVO ANTES
    spykiller = SpyKiller(
        my_name="Benjamin Arratia Uribe",
        my_username="baarratia",
        url="http://assistance-py.herokuapp.com"
    )

    ConsoleApp(spykiller).run()
