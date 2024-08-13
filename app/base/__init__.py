from flask import Blueprint


base = Blueprint('base', __name__)
from ..routes import *
