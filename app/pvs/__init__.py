from flask import Blueprint

pvs_bp = Blueprint('pvs', __name__)


from app.pvs import routes