from flask import request, make_response
from . import api
from db import User, Paciente

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
    return "correcto"

@api.route("/paciente", methods=["PUT"])
def update_paciente():
    return ""

@api.route("/pacientes", methods=["GET"])
def list_pacientes():
    return ""

@api.route("/paciente/<id>", methods=["GET"])
def get_paciente(id):
    return ""