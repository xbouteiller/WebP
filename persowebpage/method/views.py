# Core / views.py
from flask import render_template, request, Blueprint

method = Blueprint('method', __name__)

@method.route('/method')
def methods():
    return render_template('method.html')

@method.route('/method/sampling_cambium')
def cambium():
    return render_template('cambium.html')

@method.route('/method/sandblasting_seeds')
def sandblasting():
    return render_template('sandblasting.html')
