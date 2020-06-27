# Core / views.py
from flask import render_template, request, Blueprint

teaching = Blueprint('teaching', __name__)


@teaching.route('/teaching')
def teachings():
    return render_template("teaching.html")

@teaching.route('/teaching/Programming')
def programming():
    return render_template("programming.html")

@teaching.route('/teaching/statistics')
def stat():
    return render_template("statistics.html")
