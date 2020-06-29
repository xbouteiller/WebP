# Core / views.py
from flask import render_template, request, Blueprint

contact = Blueprint('contact', __name__)

@contact.route('/contact')
def cont():
    return render_template("contact.html")
