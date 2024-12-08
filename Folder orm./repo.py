import orm.modelos as modelos #accedemos a modelos.py
from sqlalchemy.orm import Session
from sqlalchemy import and_

# ALUMNOS MOSTRAR

# SELECT * FROM app.alumnos
def devuelve_alumnos(sesion:Session):
    print("SELECT * FROM app.alumnos")
    return sesion.query(modelos.Alumno).all()

# SELECT * FROM app.alumnos WHERE id={id_al}
def alumno_por_id(sesion:Session, id_usuario:int):
    print("SELECT * FROM app.alumnos WHERE id = ", id_usuario)
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

