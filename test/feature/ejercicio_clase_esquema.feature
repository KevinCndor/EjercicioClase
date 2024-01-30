# language: es
# Created by j-ken at 29/1/2024

Característica: : Calificar trabajo final de verificacion y validacion
  Como profesor
  Quiero calificar el trabajo final de mis estudiantes estrictamente
  Para aprobar a los estudiantes que demuestran el conocimiento de la materia

  Esquema del escenario: Escenario: : Profesor califica personalmente
    Dado que un alumno ha entregado su trabajo final <tipo_entrega>
    Cuando asigno una calificacion de <nota_trabajo> sobre <nota_maxima> basado en una rúbrica
    Entonces el estudiante obtendra <estado_alumno> de acuerdo a la nota de aprobacion
    Ejemplos:
      |  tipo_entrega  | nota_maxima | nota_trabajo | estado_alumno|
      |   a tiempo     |      10     |       7      |   Aprobado   |
      |  con retraso   |      8      |       7      |   Aprobado   |
      |   adelantado   |      10     |       6      |   Aprobado   |
      |  con permiso   |      10     |       6      |   Aprobado   |
      |   a tiempo     |      10     |       3      |   Reprobado  |