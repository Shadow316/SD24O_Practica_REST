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
    return sesion.query(modelos.Alumno).filter(modelos.Alumno.id == id_usuario).first()

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
    return session.query(modelos.Foto).filter(modelos.Alumno.id == id_alumno).first()

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
    return session.query(modelos.Calificacion).filter(modelos.Alumno.id == id_alumno).first()

# DELETES

# DELETE FROM app.alumnos WHERE id_alumnos={id_al}
def borra_alumno_por_id(session:Session, id_alumno:int):
    print ("DELETE FROM app.alumnos WHERE id_alumnos = ", id_alumno)
    
    return