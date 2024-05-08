from flask import request, make_response
from . import api
from db import User, Doctor
import json

@api.route("/doctor", methods=["POST"])
def create_doctor():
    data = request.get_json()
    user = User(
        name=data.get("name",""),
        lastname=data.get("lastname",""),
        age=data.get("age",0),
        document=data.get("document",""),
        email=data.get("email",""),
    )
    user.insert()
    doctor = Doctor(
        id=user.id,
        speciality= data.get("speciality","general")
    )
    doctor.insert()
    return make_response({
            "message": "doctor creado"
        }, 200)

@api.route("/doctor/<id>", methods=["PUT"])
def update_doctor(id):
    data = request.get_json()
    doctor = Doctor.query.get(id)
    if not doctor:
        return make_response({
            "message": "doctor no encontrado"
        }, 404)
    user = User.query.get(id)
    for key,value in data.items():
        if hasattr(user, key):
            setattr(user, key, value)
    user.update()
    return make_response({
            "message": "doctor actualizado"
        }, 200)

@api.route("/doctor/<id>", methods=["DELETE"])
def delete_doctor(id):
    doctor = Doctor.query.get(id)
    if not doctor:
        return make_response({
            "message": "doctor no encontrado"
        }, 404)
    user = User.query.get(id)
    doctor.delete()
    user.delete()
    return make_response({
            "message": "doctor eliminado"
        }, 200)


@api.route("/doctors", methods=["GET"])
def list_doctors():
    doctors = Doctor.query.all()
    response = []
    for doctor in doctors:
        data = User.query.get(doctor.id).__dict__
        data.pop("_sa_instance_state")
        response.append(data)
    return make_response({
            "data": response
        }, 200)

@api.route("/doctor/<id>", methods=["GET"])
def get_doctor(id):
    doctor = Doctor.query.get(id)
    if not doctor:
        return make_response({
            "message": "doctor no encontrado"
        }, 404)
    user = User.query.get(id)
    response = user.__dict__
    response.pop("_sa_instance_state")
    return make_response(response, 200)