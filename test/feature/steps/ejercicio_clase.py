from behave import *

from modelos.modelos import Alumno, Actividad, Profesor

use_step_matcher("re")

"""@step("que un alumno ha entregado su trabajo final a tiempo")
def step_impl(context):
    # debe existir un alumno
    context.alumno = Alumno("nombre")
    context.actividad_final = Actividad("proyecto final")
    context.alumno.entregar_trabajo_final(context.actividad_final)
    assert (context.actividad_final.esta_entregado_a_tiempo_la_actividad(context.alumno.actividad_final) == True)

@step("el profesor asigna una calificacion sobre 10 basado en una rúbrica")
def step_impl(context):
    # profesor recibe trabajo final
    context.profesor = Profesor("nombre")
    context.profesor.calificar_trabajo_basado_en_rubrica(context.alumno.actividad_final)
    assert (context.alumno.actividad_final.calificacion >= 0)


@step("apruebo al estudiante si la calificacion es mayor o igual a 7")
def step_impl(context):
    context.profesor.aprobar_alumno(context.alumno)
    assert (context.alumno.aprueba == True)


@step("si no cumple este minimo, repruebo al estudiante")
def step_impl(context):
    context.profesor.aprobar_alumno(context.alumno)
    assert (context.alumno.aprueba == False)
    
"""