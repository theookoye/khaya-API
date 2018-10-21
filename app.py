from models import *
from imports import app, json, redirect, request, keen, jsonify, db, hashpw, salt
from functions import doLogin

"""Routed functions"""


@app.route('/login', methods=('GET', 'POST'))
def login():

    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password')

        return doLogin(email, password)


if __name__ == '__main__':
    app.run(debug=True)
