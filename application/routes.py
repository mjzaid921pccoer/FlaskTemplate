from application import appServer

from modules.testvar import printHello

from flask import render_template, redirect, url_for, request, flash, session, jsonify

@appServer.route('/')
def homepage():
    return render_template('index.html')

@appServer.route('/hi')
def hey():
    return printHello()

#@appServer.route('/#', methods=['GET', 'POST'])
#route for get post
