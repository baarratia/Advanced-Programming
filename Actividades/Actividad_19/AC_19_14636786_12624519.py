import csv


class Estudiante:
    def __init__(self, nombre, paterno, materno):
        self.nombre = nombre
        self.paterno = paterno
        self.materno = materno
        print('{0},{1},{2}'.format(self.nombre, self.paterno, self.materno))


class RescueSiding:
    def __init__(self, file_name='alumnos.csv'):
        self.students = [student for student in self.lector(file_name)]

    def lector(self, file_name='alumnos.csv'):
        with open(file_name) as file:
            reader = csv.DictReader(file)
            for row in reader:
                nombre = self.preparar_string(row['Nombre'])
                paterno = self.preparar_string(row['Apellido paterno'])
                materno = self.preparar_string(row['Apellido materno'])
                yield (Estudiante(nombre, paterno, materno))

    @classmethod
    def preparar_string(cls, string):
        result = cls.pasar_a_mayusculas(string)
        result = cls.corregir_numero_de_erres(result)
        result = cls.remover_numero_random_if_present(result)
        return result

    @classmethod
    def remover_numero_random_if_present(cls, string):
        x = string.split(' ')
        for i in x:
            if not i.isalpha():
                r = string.partition(' ')
                string = r[2]
                return string
        return string

    @classmethod
    def corregir_numero_de_erres(cls, string):
        string = string.replace('RR', 'R')
        return string

    @classmethod
    def pasar_a_mayusculas(cls, string):
        string = string.upper()
        return string

    def to_latex(self, file_name='alumnos.tex'):
        file = open(file_name, 'w')
        file.write('''```tex\n
\\begin{table}[h]\n
\\begin{tabular}{|l|l|l|}\n
\\hline\n''')
        file.write('{0:<20s} &{0:<20s}&{0:<20s}\\\ \\hline\n'.format('Apellido paterno', 'Apellido materno', 'Nombre'))
        for i in self.students:
            file.write('{0:<20s} &{0:<20s}&{0:<20s}\\\ \\hline\n'.format(i.paterno, i.materno, i.nombre))
        file.write('''`\\end{tabular}\n
\\end{table}\n
```''')
        file.close()

    def to_html(self, file_name='alumnos.html'):
        pass

    def to_markdown(self, file_name='alumnos.md'):
        file = open(file_name, 'w')
        file.write('''```md\n''')
        file.write('| {0:<20s} | {0:<20s}| {0:<20s} |\n'.format('Apellido paterno', 'Apellido materno', 'Nombre'))
        file.write('''|-----------------------|------------------------|------|\n''')
        for i in self.students:
            file.write('| {0:<20s} | {0:<20s}| {0:<20s} |\n'.format(i.paterno, i.materno, i.nombre))
        file.write('''```\n''')
        file.close()


if __name__ == '__main__':
    rescue_siding = RescueSiding()
    rescue_siding.to_latex()
    rescue_siding.to_html()
    rescue_siding.to_markdown()
