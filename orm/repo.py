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
    return session.query(modelos.Calificacion).filter(modelos.Calificacion.id == id_calificacion).all()

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
