from flask import jsonify
from marshmallow import ValidationError
from ma import ma
from db import db   

from server.instance import server

api = server.api
app = server.app


