from pydantic import BaseModel

# Definimos el esquema del alumno
class AlumnoBase(BaseModel):   
    nombre:str
    edad:int
    domicilio:str
    carrera:str
    trimestre:str
    email:str
    password:str

# Definimos el esquema de las calificaciones
class CalificacioneBase(BaseModel):
    id_alumno:int
    uea:str
    calificacion:str

# Definimos el esquema de las fotos
class FotoBase(BaseModel):
    id_alumno:int
    titulo:str
    descripcion:str
    ruta:str

# Se crearon los esquemas para práctica 2