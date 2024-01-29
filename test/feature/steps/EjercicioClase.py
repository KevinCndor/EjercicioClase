from behave import *

use_step_matcher("re")


@step("que un alumno ha entregado su trabajo final a tiempo")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Dado que un alumno ha entregado su trabajo final a tiempo')


@step("el profesor asigna una calificacion sobre 10 basado en una rúbrica")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Cuando el profesor asigna una calificacion sobre 10 basado en una rúbrica')


@step("apruebo al estudiante si la calificacion es mayor o igual a 7")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Entonces apruebo al estudiante si la calificacion es mayor o igual a 7')


@step("si no cumple este minimo, repruebo al estudiante")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Pero si no cumple este minimo, repruebo al estudiante')