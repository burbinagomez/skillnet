from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import ForeignKey

class Base(DeclarativeBase):
  def insert(self):
    db.session.add(self)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

db = SQLAlchemy(model_class=Base)

class User(db.Model):
  __tablename__ = "user"
  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str]
  lastname: Mapped[str]
  age: Mapped[int]
  document: Mapped[str]
  email: Mapped[str] = mapped_column(unique=True)

class Paciente(db.Model):
  __tablename__ = "paciente"
  id: Mapped[int] = mapped_column(ForeignKey("user.id"),primary_key=True)

class Doctor(db.Model):
  __tablename__ = "doctor"
  id: Mapped[int] = mapped_column(ForeignKey("user.id"),primary_key=True)
  speciality: Mapped[str]

class Cita(db.Model):
  __tablename__ = "cita"
  id: Mapped[int] = mapped_column(primary_key=True)
  date: Mapped[str]
  paciente: Mapped[int] = mapped_column(ForeignKey("paciente.id"))
  doctor: Mapped[int] = mapped_column(ForeignKey("doctor.id"))