# Core / views.py
from flask import render_template, request, Blueprint

research = Blueprint('research', __name__)


@research.route('/research')
def researchs():
    return render_template("research.html")

@research.route('/research/invasive_species')
def invasive():
    return render_template("invasive.html")

@research.route('/research/drought_resitance')
def drought():
    return render_template("drought.html")
