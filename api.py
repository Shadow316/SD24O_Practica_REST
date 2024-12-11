from fastapi import FastAPI, UploadFile, File, Form, Depends
from typing import Optional
from pydantic import BaseModel
import shutil
import os
import uuid
import orm.repo as repo # Función para hacer las consultas a la BD
import orm.esquemas as esquemas
from sqlalchemy.orm import Session
from sqlalchemy import and_
from orm.config import generador_sesion # Generador de sesiones

# Se crea el servidor
app = FastAPI()

class Base(BaseModel):
    user: str

# ALL GET

# get("/alumnos”)
@app.get("/alumnos")
def lista_alumnos(sesion:Session=Depends(generador_sesion)):
    print("API consultando a los alumnos.")
    return repo.devuelve_alumnos(sesion)

# get("/alumnos/{id})
@app.get("/alumnos/{id}")
def alumno_por_id(id:int, sesion:Session=Depends(generador_sesion)):
    print("API consultando alumnos por id")
    return repo.alumno_por_id(sesion, id)

# get("/alumnos/{id}/calificaciones")
@app.get("/alumnos/{id}/calificaciones")
def calificaciones_por_id_alumno(id:int, sesion:Session=Depends(generador_sesion)):
    print("Api consultando calificaciones por id del alumno")
    return repo.calificaciones_por_id_alumno(sesion, id)

# get("/alumnos/{id}/fotos")
@app.get("/alumnos/{id}/fotos")
def fotos_por_id_alumno(id:int, sesion:Session=Depends(generador_sesion)):
    print("Api consultando fotos por id del alumno")
    return repo.foto_por_id_alumnos(sesion, id)

# get("/fotos/{id}”)
@app.get("/fotos/{id}")
def fotos_por_id(id:int, sesion:Session=Depends(generador_sesion)):
    print("Api consultando todas las fotos")
    return repo.foto_por_id(sesion, id)

# get("/calificaciones/{id}”)
@app.get("/calificaciones/{id}")
def calificaciones_por_id(id:int, sesion:Session=Depends(generador_sesion)):
    print("Api consultando calificaciones por id")
    return repo.calificaciones_por_id(sesion, id)

# ALL DELETE

# delete("/fotos/{id}”)
@app.delete("/fotos/{id}")
def borrar_foto_por_id(id:int, sesion:Session=Depends(generador_sesion)):
    repo.borra_fotos_por_id(sesion, id)
    return {"Status_borrado, ok"}

# delete("/calificaciones/{id}”)
@app.delete("/calificaciones/{id}")
def borrar_calificacion_por_id(id:int, sesion:Session=Depends(generador_sesion)):
    repo.borra_calificaciones_por_id(sesion, id)
    return {"Status_borrado, ok"}

# delete("/alumnos/{id}/calificaciones")
@app.delete("/alumnos/{id}/calificaciones")
def borrar_calificacion_por_id_alumno(id:int, sesion:Session=Depends(generador_sesion)):
    repo.borra_calificaciones_por_id_alumnos(sesion, id)
    return {"Status_borrado, ok"}

# delete("/alumnos/{id}/fotos")
@app.delete("/alumnos/{id}/fotos")
def borrar_foto_por_id_alumno(id:int, sesion:Session=Depends(generador_sesion)):
    repo.borra_fotos_por_id_alumnos(sesion, id)
    return{"Status_borrado, ok"}

# delete("/alumnos/{id})
@app.delete("/alumnos/{id}")
def borrar_alumno_por_id(id:int, sesion:Session=Depends(generador_sesion)):
    repo.borra_calificaciones_por_id_alumnos(sesion, id)
    repo.borra_fotos_por_id_alumnos(sesion, id)
    repo.borra_alumno_por_id(sesion, id)
    return {"Status_borrado", "ok"}

# PRACTICA 2

# post("/alumnos”)
@app.post("/alumnos")
def guardar_alumno(alumno:esquemas.AlumnoBase, sesion:Session=Depends(generador_sesion)):
    print(alumno)
    return repo.guardar_alumno(sesion, alumno)

# put("/alumnos/{id})
@app.put("/alumnos/{id}")
def actualizar_alumno(id:int, info_alumno:esquemas.AlumnoBase, sesion:Session=Depends(generador_sesion)):
    return repo.actualizar_alumno(sesion, id, info_alumno)

# post("/alumnos/{id}/calificaciones")
@app.post("/alumnos/{id}/calificaciones")
def guardar_calificacion_por_id_alumno(id:int, calificacion:esquemas.CalificacioneBase, sesion:Session=Depends(generador_sesion)):
    return repo.guardar_calificacion_por_id_alumno(sesion, id, calificacion)

# put("/calificaciones/{id}")
@app.put("/calificaciones/{id}")
def actualizar_calificacion_por_id(id:int, info_calificacion:esquemas.CalificacioneBase, sesion:Session=Depends(generador_sesion)):
    return repo.actualizar_calificacion_por_id(sesion, id, info_calificacion)