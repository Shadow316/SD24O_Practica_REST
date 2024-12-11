import orm.esquemas as esquemas
import orm.modelos as modelos #accedemos a modelos.py
from sqlalchemy.orm import Session
from sqlalchemy import and_

# ALUMNOS MOSTRAR

# SELECT * FROM app.alumnos
def devuelve_alumnos(sesion:Session):
    print("SELECT * FROM app.alumnos")
    return sesion.query(modelos.Alumno).all()

# SELECT * FROM app.alumnos WHERE id={id_al}
def alumno_por_id(sesion:Session, id_alumno:int):
    print("SELECT * FROM app.alumnos WHERE id = ", id_alumno)
    return sesion.query(modelos.Alumno).filter(modelos.Alumno.id == id_alumno).first()

# FOTOS MOSTRAR

# SELECT * FROM app.fotos
def devuelve_fotos(session:Session):
    print("SELECT * FROM app.fotos")
    return session.query(modelos.Foto).all()

# SELECT * FROM app.fotos WHERE id={id_fo}
def foto_por_id(session:Session, id_foto:int):
    print("SELECT * FROM app.fotos WHERE id = ", id_foto)
    return session.query(modelos.Foto).filter(modelos.Foto.id == id_foto).first()

# SELECT * FROM app.fotos WHERE id_alumnos={id_al}
def foto_por_id_alumnos(session:Session, id_alumno):
    print("SELECT * FROM app.fotos WHERE id_alumnos = ", id_alumno)
    return session.query(modelos.Foto).filter(modelos.Foto.id_alumno == id_alumno).all()

# CALIFICACIONES MOSTRAR

# SELECT * FROM app.calificaciones
def devuelve_calificaciones(session:Session):
    print("SELECT * FROM app.calificaciones")
    return session.query(modelos.Calificacion).all()

# SELECT * FROM app.calificaciones WHERE id={id_fo}
def calificaciones_por_id(session:Session, id_calificacion:int):
    print("SELECT * FROM app.calificaciones WHERE id = ", id_calificacion)
    return session.query(modelos.Calificacion).filter(modelos.Calificacion.id == id_calificacion).first()

# SELECT * FROM app.calificaciones WHERE id_alumnos={id_al}
def calificaciones_por_id_alumno(session:Session, id_alumno:int):
    print("SELECT * FROM app.calificaciones WHERE id_alumnos = ", id_alumno)
    return session.query(modelos.Calificacion).filter(modelos.Calificacion.id_alumno == id_alumno).all()

# DELETES

# DELETE FROM app.alumnos WHERE id_alumnos={id_al}
def borra_alumno_por_id(session:Session, id_alumno:int):
    print ("DELETE FROM app.alumnos WHERE id_alumnos = ", id_alumno)
    alu = alumno_por_id(session, id_alumno)
    if alu is not None:
        session.delete(alu)
        session.commit()
    
    respuesta = {
        "mensaje" : "Alumno eliminado"
    }

    return respuesta

# DELETE FROM app.calificaciones WHERE id_alumnos={id_al}
def borra_calificaciones_por_id_alumnos(session:Session, id_alumno:int):
    print("DELETE FROM app.calificaciones WHERE id_alumnos = ", id_alumno)
    cali = calificaciones_por_id_alumno(session, id_alumno)
    if cali is not None:
        session.delete(cali)
        session.commit()

    respuesta = {
        "mensaje" : "Calificacion borrada por id de Alumno"
    }
    return respuesta

# DELETE FROM app.fotos WHERE id_alumnos={id_al}
def borra_fotos_por_id_alumnos(session:Session, id_alumno:int):
    print("DELETE FROM app.fotos WHERE id_alumnos = ", id_alumno)
    foto = foto_por_id_alumnos(session, id_alumno)
    if foto is not None:
        session.delete(foto)
        session.commit()

    respuesta = {
        "mensaje" : "Foto borrada por id de Alumno"
    }
    return respuesta

# Adicionales

# DELETE FROM app.fotos WHERE id = {id}
def borra_fotos_por_id(session:Session, id:int):
    print("DELETE FROM app.fotos WHERE id =" , id)
    bfoto = foto_por_id(session, id)
    if bfoto is not None:
        session.delete(bfoto)
        session.commit()

    respuesta = {
        "mensaje" : "Foto borrada por id"
    }
    return respuesta

# DELETE FROM app.calificaciones WHERE id = {id}
def borra_calificaciones_por_id(session:Session, id:int):
    print("DELETE FROM app.calificaciones WHERE id = ", id)
    bcali = calificaciones_por_id(session, id)
    if bcali is not None:
        session.delete(bcali)
        session.commit()

    respuesta = {
        "mensaje" : "Calificación borrada por id"
    }
    return respuesta

# PRACTICA 2

# post
def guardar_alumno(session:Session, alu_nuevo:esquemas.AlumnoBase): 
    alu_bd = modelos.Alumno()
    alu_bd.nombre = alu_nuevo.nombre
    alu_bd.edad = alu_nuevo.edad
    alu_bd.domicilio = alu_nuevo.domicilio
    alu_bd.carrera = alu_nuevo.carrera
    alu_bd.trimestre = alu_nuevo.trimestre
    alu_bd.email = alu_nuevo.email
    alu_bd.password = alu_nuevo.password

    session.add(alu_bd)
    session.commit()
    session.refresh(alu_bd)
    return alu_bd

# put
def actualizar_alumno(sesion:Session, id_alumno:int, alu_esquema:esquemas.AlumnoBase): 
    alu_db = alumno_por_id(sesion, id_alumno)
    if alu_db is not None:
        alu_db.nombre = alu_esquema.nombre
        alu_db.edad = alu_esquema.edad
        alu_db.domicilio = alu_esquema.domicilio
        alu_db.carrera = alu_esquema.carrera
        alu_db.trimestre = alu_esquema.trimestre
        alu_db.email = alu_esquema.email
        alu_db.password = alu_esquema.password
        sesion.commit()
        sesion.refresh(alu_db)
        print(alu_esquema)
        return alu_esquema
    else:
        respuesta = {"mensaje" : "No existe el alumno"}
        return respuesta

# post("/alumnos/{id}/calificaciones")
def guardar_calificacion_por_id_alumno(sesion:Session, id_alumno:int, cal_nueva:esquemas.CalificacioneBase):
    cal_bus = alumno_por_id(sesion, id_alumno)
    cal_bd = modelos.Calificacion()
    if cal_bus is not None:
        cal_bd.id_alumno = id_alumno
        cal_bd.uea = cal_nueva.uea
        cal_bd.calificacion = cal_nueva.calificacion
        sesion.add(cal_bd)
        sesion.commit()
        sesion.refresh(cal_bd)
        return cal_bd
    else:
        respuesta = {"mensaje" : "No hay alumno para actualizar calificación"}
        return respuesta

# put
def actualizar_calificacion_por_id(sesion:Session, id_calificacion:int, calificacion_esquema:esquemas.CalificacioneBase):
    cal_bd = calificaciones_por_id(sesion, id_calificacion)
    if cal_bd is not None:
        cal_bd.id_alumno = calificacion_esquema.id_alumno
        cal_bd.uea = calificacion_esquema.uea
        cal_bd.calificacion = calificacion_esquema.calificacion
        sesion.commit()
        sesion.refresh(cal_bd)
        print(calificacion_esquema)
        return calificacion_esquema
    else:
        respuesta = {"mensaje" : "No existe la calificación"}
        return respuesta
    
    
# post("/alumnos/{id}/fotos")
def guardar_foto_por_id_alumno(sesion:Session, id_alumno:int, foto_nueva:esquemas.FotoBase):
    foto_bus = alumno_por_id(sesion, id_alumno)
    foto_bd = modelos.Foto()
    if foto_bus is not None:
        foto_bd.id_alumno = id_alumno
        foto_bd.titulo = foto_nueva.titulo
        foto_bd.descripcion = foto_nueva.descripcion
        foto_bd.ruta = foto_nueva.ruta
        sesion.add(foto_bd)
        sesion.commit()
        sesion.refresh(foto_bd)
        return foto_bd
    else:
        respuesta = {"mensaje" : "No hay alumno para actualizar foto"}
        return respuesta
    
# put("/fotos/{id}")
def actualizar_foto_por_id(sesion:Session, id_foto, foto_esquema:esquemas.FotoBase):
    foto_bd = foto_por_id(sesion, id_foto)
    if foto_bd is not None:
        foto_bd.id_alumno = foto_esquema.id_alumno
        foto_bd.titulo = foto_esquema.titulo
        foto_bd.descripcion = foto_esquema.descripcion
        foto_bd.ruta = foto_esquema.ruta
        sesion.commit()
        sesion.refresh(foto_bd)
        print(foto_esquema)
        return foto_esquema
    else:
        respuesta = {"mensaje" : "No existe la foto"}
        return respuesta