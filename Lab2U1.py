
from ast import Index
import random
from re import X


class Estudiante():

    def __init__(self, nombre) -> None:

        self.nombre = nombre
        self.asignaturas = []
        self.diplomas_a_cambiar = []
        self.diplomas_propios = []

    def inscribe_asignatura(self, asignatura):
        self.asignaturas.append(asignatura)


    def get_asignaturas(self):
        return self.asignaturas

    def get_lista_diplomas(self):
        return self.diplomas_a_cambiar

    def recibir_diploma(self, diploma):
        self.diplomas_a_cambiar.append(diploma)
    
    def encontrar_diploma(self, diploma):
        self.diplomas_a_cambiar.remove(diploma)
        self.diplomas_propios.append(diploma)


class Asignatura():

    def __init__(self, nombre_asignatura) -> None:
        self.nombre_asignatura = nombre_asignatura
        self.alumnos_inscritos = []
        self.diplomas_entregados = []
    

    def inscribe_alumno(self, alumno):
        self.alumnos_inscritos.append(alumno)
    

    def get_lista_alumnos(self):
        return self.alumnos_inscritos
    
    def get_nombre(self):
        return self.nombre_asignatura


class Diplomas():

    def __init__(self, estudiante, asignatura) -> None:
        self.estudiante = estudiante
        self.asignatura = asignatura

    def get_nombre_alumno(self):
        return self.estudiante
    
    def get_asignatura(self):
        return self.asignatura


def inscribe_asignatura(lista_alumnos, asignatura):

    # estudiantes 
    for x in range(0,(len(lista_alumnos))//2):
        alumno_seleccionado = random.randint(0,len(lista_alumnos)-1)
        #print(type(alumno_seleccionado))
        if lista_alumnos[alumno_seleccionado] not in asignatura.get_lista_alumnos():
            asignatura.inscribe_alumno(lista_alumnos[alumno_seleccionado])
            lista_alumnos[alumno_seleccionado].inscribe_asignatura(asignatura)
        else:
            x -= 1


def crea_diplomas(asignatura, lista_diplomas):

    lista = asignatura.get_lista_alumnos()
    for x in range(0,3):
        alumno_seleccionado = random.randint(0,len(lista)-1)
        #print(type(alumno_seleccionado))
        if lista[alumno_seleccionado] not in lista_diplomas:
            diploma = Diplomas(lista[alumno_seleccionado], asignatura)
            lista_diplomas.append(diploma)


def generador():
    x = 1
    while x > 0:
        yield x
        x += 1


def entrega_diplomas(lista_diplomas, lista_alumnos):
    for x in generador():
        if len(lista_diplomas) > 0:
            entregar = random.randint(0,len(lista_diplomas)-1)
            diploma_entregado = lista_diplomas[entregar]
            lista_diplomas.pop(entregar)
            lista_alumnos[x-1].recibir_diploma(diploma_entregado)
        else:
            break

    
def revisar_diploma_propio(estudiante):

    for item in estudiante.get_lista_diplomas():
        if item.get_nombre_alumno().nombre == estudiante.nombre:
            estudiante.encontrar_diploma(item)

def cambiar_diploma(lista_cambiar):
    try:
        for x in range(0, len(lista_cambiar)-1,2):
            diploma1 = lista_cambiar[x].get_lista_diplomas()[0]
            diploma2 = lista_cambiar[x+1].get_lista_diplomas()[0]
            
            lista_cambiar[x].get_lista_diplomas().remove(diploma1)
            lista_cambiar[x+1].get_lista_diplomas().remove(diploma2)
            lista_cambiar[x].get_lista_diplomas().append(diploma2)
            lista_cambiar[x+1].get_lista_diplomas().append(diploma1)

    except IndexError:
        pass




def main():

    lista_alumnos = []
    lista_diplomas = []


    for x in range(0,15):
        alumno = Estudiante(x)
        lista_alumnos.append(alumno)

    print("lista alumnos es")
    print(len(lista_alumnos))
    for item in lista_alumnos:
        print(item.nombre)
    
    fisica = Asignatura("fisica")
    programacion = Asignatura("programacion")
    calculo = Asignatura("calculo")
    bioquimica = Asignatura("bioquimica")

    inscribe_asignatura(lista_alumnos, fisica)
    inscribe_asignatura(lista_alumnos, programacion)
    inscribe_asignatura(lista_alumnos, calculo)
    inscribe_asignatura(lista_alumnos, bioquimica)

    # inscribir alumnos que no tengan ninguna asignatura
    for alumno in lista_alumnos:
        if len(alumno.asignaturas) == 0:
            pass


    print("los alumnos inscritos son")

    for item in fisica.get_lista_alumnos():
        print(item.nombre)

    for item in fisica.get_lista_alumnos():
        for x in item.get_asignaturas():
            print(x.get_nombre())

    
    crea_diplomas(fisica, lista_diplomas)
    crea_diplomas(calculo, lista_diplomas)
    crea_diplomas(programacion, lista_diplomas)
    crea_diplomas(bioquimica, lista_diplomas)

    print("los diplomas creados son")
    for item in lista_diplomas:
        print(item.get_nombre_alumno().nombre)

    entrega_diplomas(lista_diplomas, lista_alumnos)

    for x in range(0,1):
        for alumno in lista_alumnos:
            revisar_diploma_propio(alumno)

        print("---------------")

        for alumno in lista_alumnos:
            print(alumno.diplomas_propios)
        
        lista_cambiar_diploma = []
        for alumno in lista_alumnos:
            if len(alumno.diplomas_a_cambiar) > 0:
                lista_cambiar_diploma.append(alumno)
        
        cambiar_diploma(lista_cambiar_diploma)

    for alumno in lista_alumnos:
        revisar_diploma_propio(alumno)

    print("---------------")

    for alumno in lista_alumnos:
        print(alumno.diplomas_propios)

    print("---------------")

    for item in fisica.alumnos_inscritos:
        print(item.nombre)


    



if __name__ == "__main__":

    main()

