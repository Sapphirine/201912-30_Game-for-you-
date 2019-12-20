#!/usr/bin/env python3

import flask
from flask import render_template
import json
import sys
import api

app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/home/<username>/<password>')
def homepage(username, password):
    result = api.checkUser(username, password)
    if result:
        return render_template("Bigdata.html")
    else:
        return render_template('login.html')

@app.route('/signup/<username>/<password>')
def signup(username, password):
    res = api.creatUser(username, password)
    return render_template('login.html')

@app.route('/search_result/name/<search_key>')
def searchResultByName(search_key):
    result_list = api.searchByKeyName(search_key)
    return render_template("Bigdata_search_reasult.html", game_list=result_list)

@app.route('/search_result/platform/<search_key>')
def searchResultByPlatform(search_key):
    result_list = api.searchByKeyPlatform(search_key)
    return render_template("Bigdata_search_reasult.html", game_list=result_list)

@app.route('/game/<game_name>/<game_platform>')
def game_tem(game_name, game_platform):
    game_info = api.searchByTem(game_name, game_platform)
    return render_template('Bigdata_game.html', target_game=game_info)

@app.route('/game/<game_name>')
def game_name(game_name):
    game_info = api.searchByName(game_name)
    return render_template('Bigdata_game.html', target_game=game_info)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=int(port))