# Core / views.py
from flask import render_template, request, Blueprint

vitae = Blueprint('vitae', __name__)

@vitae.route('/vitae')
def cv():
    return render_template("vitae.html")
