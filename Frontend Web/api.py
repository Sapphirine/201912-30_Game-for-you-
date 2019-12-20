import flask
from flask import render_template
import json
import sys
import psycopg2


app = flask.Flask(__name__)

database =
user =
password = 

@app.route('/search_result/name/<name>')
def searchByKeyName(name):

    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
    except Exception as e:
        print(e)
        exit()

    try:
        cursor = connection.cursor()
        query = "SELECT * FROM bigdata_database WHERE lower(title) LIKE %s order by userscore desc"
        cursor.execute(query, ("%"+name.lower()+"%",))
    except Exception as e:
        print('Cursor error: {}'.format(e))
        connection.close()
        exit()

    gameList = []

    for row in cursor:
        gamedic = {}
        title, year, publisher, genre, platform, no_Players, userscore, labels, recommendation = row
        labels = labels.split(',')
        res = []
        for l in labels:
            res.append(l.capitalize())
        labels = ", ".join(res)
        gamedic["title"] = title
        gamedic["year"] = year
        gamedic["publisher"] = publisher
        gamedic["genre"] = " ".join(genre.split(";"))
        gamedic["platform"] = platform
        gamedic["no_Players"] = no_Players
        gamedic["userscore"] = userscore
        gamedic["labels"] = labels
        gamedic["recommendation"] = recommendation.split(',')
        gameList.append(gamedic)

    connection.close()
    return gameList

@app.route('/search_result/platform/<platform>')
def searchByKeyPlatform(platform):

    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
    except Exception as e:
        print(e)
        exit()

    try:
        cursor = connection.cursor()
        query = "SELECT * FROM bigdata_database WHERE lower(platform) LIKE %s order by userscore desc"
        cursor.execute(query, ("%"+platform.lower()+"%",))
    except Exception as e:
        print('Cursor error: {}'.format(e))
        connection.close()
        exit()

    gameList = []

    for row in cursor:
        gamedic = {}
        title, year, publisher, genre, platform, no_Players, userscore, labels, recommendation = row
        labels = labels.split(',')
        res = []
        for l in labels:
            res.append(l.capitalize())
        labels = ", ".join(res)
        gamedic["title"] = title
        gamedic["year"] = year
        gamedic["publisher"] = publisher
        gamedic["genre"] = " ".join(genre.split(";"))
        gamedic["platform"] = platform
        gamedic["no_Players"] = no_Players
        gamedic["userscore"] = userscore
        gamedic["labels"] = labels
        gamedic["recommendation"] = recommendation.split(',')
        gameList.append(gamedic)

    connection.close()
    return gameList

@app.route('/search/<name>/<platform>')
def searchByTem(name, platform):

    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
    except Exception as e:
        print(e)
        exit()

    try:
        cursor = connection.cursor()
        query = "SELECT * FROM bigdata_database WHERE title = %s and platform= %s"
        cursor.execute(query, (name, platform))
    except Exception as e:
        print('Cursor error: {}'.format(e))
        connection.close()
        exit()

    gameList = []

    for row in cursor:
        gamedic = {}
        title, year, publisher, genre, platform, no_Players, userscore, labels, recommendation = row
        labels = labels.split(',')
        res = []
        for l in labels:
            res.append(l.capitalize())
        labels = ", ".join(res)
        gamedic["title"] = title
        gamedic["year"] = year
        gamedic["publisher"] = publisher
        gamedic["genre"] = " ".join(genre.split(";"))
        gamedic["platform"] = platform
        gamedic["no_Players"] = no_Players
        gamedic["userscore"] = userscore
        gamedic["labels"] = labels
        gamedic["recommendation"] = recommendation.split(',')
        gameList.append(gamedic)

    connection.close()
    return gameList[0]

@app.route('/search/<name>')
def searchByName(name):

    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
    except Exception as e:
        print(e)
        exit()

    try:
        cursor = connection.cursor()
        query = "SELECT * FROM bigdata_database WHERE title = %s"
        cursor.execute(query, (name, ))
    except Exception as e:
        print('Cursor error: {}'.format(e))
        connection.close()
        exit()

    gameList = []

    for row in cursor:
        gamedic = {}
        title, year, publisher, genre, platform, no_Players, userscore, labels, recommendation = row
        labels = labels.split(',')
        res = []
        for l in labels:
            res.append(l.capitalize())
        labels = ", ".join(res)
        gamedic["title"] = title
        gamedic["year"] = year
        gamedic["publisher"] = publisher
        gamedic["genre"] = " ".join(genre.split(";"))
        gamedic["platform"] = platform
        gamedic["no_Players"] = no_Players
        gamedic["userscore"] = userscore
        gamedic["labels"] = labels
        gamedic["recommendation"] = recommendation.split(',')
        gameList.append(gamedic)

    connection.close()
    return gameList[0]

def checkUser(username, p):

    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
    except Exception as e:
        print(e)
        exit()

    try:
        cursor = connection.cursor()
        query = "SELECT password FROM bigdata_users WHERE username = %s"
        cursor.execute(query, (username, ))
    except Exception as e:
        print('Cursor error: {}'.format(e))
        connection.close()
        exit()

    res = False
    for row in cursor:
        p_tmp = row[0]
        if p == p_tmp:
            res = True

    connection.close()
    return res


def creatUser(username, p):
    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
    except Exception as e:
        print(e)
        exit()

    try:
        cursor = connection.cursor()
        query = "INSERT INTO bigdata_users (username, password) VALUES (%s, %s)"
        print(username, p)
        cursor.execute(query, (username, p))
    except Exception as e:
        print('Cursor error: {}'.format(e))
        connection.close()
        exit()

    connection.close()
    return True

if __name__ == '__main__':
#    print(get_display_by_genre("Sports"))
#    print(get_name_display_by_genre("Sports"))
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=port)
