from behave import *

from modelos.modelos import Profesor, Alumno, Actividad

use_step_matcher("re")


@step("que un alumno ha entregado su trabajo final (?P<tipo_entrega>.+)")
def step_impl(context, tipo_entrega):
    # debe existir un alumno
    context.alumno = Alumno("nombre")
    context.actividad_final = Actividad("proyecto final")
    context.actividad_final.estado_entrega = tipo_entrega
    assert (context.actividad_final.estado_entrega == tipo_entrega)


@step("asigno una calificacion de (?P<nota_trabajo>.+) sobre (?P<nota_maxima>.+) basado en una rúbrica")
def step_impl(context, nota_trabajo, nota_maxima):
    context.profesor = Profesor("nombre")
    context.actividad_final = Actividad("proyecto final")
    context.profesor.calificar_trabajo_basado_en_rubrica(context.actividad_final, nota_trabajo)
    assert (context.alumno.actividad_final.nota_trabajo <= int(nota_maxima))


@step("el estudiante obtendra (?P<estado_alumno>.+) de acuerdo a la nota de aprobacion")
def step_impl(context, estado_alumno):
    context.profesor.aprobar_alumno(estado_alumno, context.alumno)
    assert (context.alumno.aprueba == True)
