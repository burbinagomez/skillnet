from flask import request, make_response
from . import api
from db import User, Cita
import json

@api.route("/cita", methods=["POST"])
def create_cita():
    data = request.get_json()
    required_fields = ["paciente","doctor", "date"]
    for field in required_fields:
        if not data.get(field):
            return make_response({
            "message": f"{field} es requerido"
        }, 402)
    cita = Cita(
        paciente= data.get("paciente","general"),
        doctor= data.get("doctor","general"),
        date= data.get("date")
    )
    cita.insert()
    return make_response({
            "message": "cita creado"
        }, 200)

@api.route("/cita/<id>", methods=["PUT"])
def update_cita(id):
    data = request.get_json()
    required_fields = ["paciente","doctor", "date"]
    for field in required_fields:
        if not data.get(field):
            return make_response({
            "message": f"{field} es requerido"
        }, 402)
    cita = Cita.query.get(id)
    if not cita:
        return make_response({
            "message": "cita no encontrado"
        }, 404)
    for key,value in data.items():
        if hasattr(cita, key):
            setattr(cita, key, value)
    cita.update()
    return make_response({
            "message": "cita actualizado"
        }, 200)

@api.route("/cita/<id>", methods=["DELETE"])
def delete_cita(id):
    cita = Cita.query.get(id)
    if not cita:
        return make_response({
            "message": "cita no encontrado"
        }, 404)
    cita.delete()
    return make_response({
            "message": "cita eliminado"
        }, 200)


@api.route("/citas", methods=["GET"])
def list_citas():
    citas = Cita.query.all()
    response = []
    for cita in citas:
        data = cita.__dict__
        data.pop("_sa_instance_state")
        response.append(data)
    return make_response({
            "data": response
        }, 200)

@api.route("/cita/<id>", methods=["GET"])
def get_cita(id):
    cita = Cita.query.get(id)
    if not cita:
        return make_response({
            "message": "cita no encontrado"
        }, 404)
    response = cita.__dict__
    response.pop("_sa_instance_state")
    return make_response(response, 200)