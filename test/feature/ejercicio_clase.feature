# Created by j-ken at 29/1/2024
  # language: es

Característica: : Calificar trabajo final de verificacion y validacion
  Como profesor
  Quiero calificar el trabajo final de mis estudiantes estrictamente
  Para aprobar a los estudiantes que demuestran el conocimiento de la materia

  Escenario: : Profesor califica personalmente
    Dado que un alumno ha entregado su trabajo final a tiempo
    Cuando el profesor asigna una calificacion sobre 10 basado en una rúbrica
    Entonces apruebo al estudiante si la calificacion es mayor o igual a 7
    Pero si no cumple este minimo, repruebo al estudiante