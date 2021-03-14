from flask import Flask

#Creating server object
appServer = Flask(__name__)

#importing routes for webapp
from application import routes