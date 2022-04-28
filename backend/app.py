from unicodedata import name
from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def hello():

    token = request.headers.get("X-Ms-Token-Aad-Access-Token")
    idp = request.headers.get("X-MS-CLIENT-PRINCIPAL-IDP")
    principal = request.headers.get("X-MS-CLIENT-PRINCIPAL")
    name = request.headers.get("X-MS-CLIENT-PRINCIPAL-NAME")    

    return  '{} {} {} {}'.format(token, idp, principal, name)
