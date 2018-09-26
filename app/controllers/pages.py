from flask import Blueprint, request, render_template

mod_pages = Blueprint('mod_pages', __name__, url_prefix='/')

@mod_pages.route('/')
def index():
    return render_template('index.html')
