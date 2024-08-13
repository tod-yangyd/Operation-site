import os
from app import create_app
from flask import render_template

app = create_app('default')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('templates/404.html'), 404

