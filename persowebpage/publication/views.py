# Core / views.py
from flask import render_template, request, Blueprint

publication = Blueprint('publication', __name__)

@publication.route('/publication')
def publi():
    return render_template("publication.html")
