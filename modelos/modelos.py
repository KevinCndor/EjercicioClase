from datetime import datetime


class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre
        self.actividad_final = Actividad("proyecto final")
        self.profesor = Profesor("nombre")
        self.aprueba = False

class Actividad:
    def __init__(self, actividad_final):
        self.estado_entrega = ""
        self.actividad_final = actividad_final
        self.nota_trabajo = 0


class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre

    def calificar_trabajo_basado_en_rubrica(self, actividad_final ,nota_trabajo):
        actividad_final.calificacion = nota_trabajo

    def aprobar_alumno(self, estado_alumno, alumno):
        if estado_alumno == "Aprobado":
            alumno.aprueba = True
        else:
            alumno.aprueba = False
