from flask import Flask, url_for, request, redirect, jsonify, url_for
from flask_cors import CORS
from itsdangerous import SignatureExpired, URLSafeTimedSerializer
from pymongo import MongoClient
from bcrypt import hashpw
from datetime import date
from os import urandom, system
import paynow
import keen
import json
import re

# Khaya Configurations

# app
app = Flask(__name__)
CORS(app)  # cross-origin reference security implementation
app.config['SECRET-KEY'] = urandom(36)
app.config.from_pyfile('config.cfg')

# mongodb
khaya = MongoClient('localhost', 27017)
db = khaya['khaya']

# keen analytics


# paynow


# bcrypt hashes
salt = b'$2b$05$iIjhPDKsIoHJC7sDr4IVLO'


# validators


# token configuration

s = URLSafeTimedSerializer('KHAYA_ZIMBABWE...')

# global variables
newpassword = None
dbEmail = ''
