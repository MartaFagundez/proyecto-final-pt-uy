"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from flask_cors import CORS
from flask_jwt_extended import jwt_required, get_jwt_identity
from dotenv import load_dotenv
import os

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)

# Cargar variables de entorno desde el archivo .env
load_dotenv()


@api.route('/hello', methods=['POST', 'GET'])
@jwt_required()
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200