from flask import request, make_response
from . import api
from db import User, Paciente
import json

@api.route("/paciente", methods=["POST"])
def create_paciente():
    data = request.get_json()
    user = User(
        name=data.get("name",""),
        lastname=data.get("lastname",""),
        age=data.get("age",0),
        document=data.get("document",""),
        email=data.get("email",""),
    )
    user.insert()
    paciente = Paciente(
        id=user.id
    )
    paciente.insert()
    return make_response({
            "message": "Paciente creado"
        }, 200)

@api.route("/paciente/<id>", methods=["PUT"])
def update_paciente(id):
    data = request.get_json()
    paciente = Paciente.query.get(id)
    if not paciente:
        return make_response({
            "message": "Paciente no encontrado"
        }, 404)
    user = User.query.get(id)
    for key,value in data.items():
        if hasattr(user, key):
            setattr(user, key, value)
    user.update()
    return make_response({
            "message": "Paciente actualizado"
        }, 200)

@api.route("/paciente/<id>", methods=["DELETE"])
def delete_paciente(id):
    paciente = Paciente.query.get(id)
    if not paciente:
        return make_response({
            "message": "Paciente no encontrado"
        }, 404)
    user = User.query.get(id)
    paciente.delete()
    user.delete()
    return make_response({
            "message": "Paciente eliminado"
        }, 200)


@api.route("/pacientes", methods=["GET"])
def list_pacientes():
    pacientes = Paciente.query.all()
    response = []
    for paciente in pacientes:
        data = User.query.get(paciente.id).__dict__
        data.pop("_sa_instance_state")
        response.append(data)
    return make_response({
            "data": response
        }, 200)

@api.route("/paciente/<id>", methods=["GET"])
def get_paciente(id):
    paciente = Paciente.query.get(id)
    if not paciente:
        return make_response({
            "message": "Paciente no encontrado"
        }, 404)
    user = User.query.get(id)
    response = user.__dict__
    response.pop("_sa_instance_state")
    return make_response(response, 200)