import os
from library import *

from flask import Flask, request, jsonify
app = Flask(__name__)
app.config["DEBUG"] = True


'''
NOTE
  Codice risposta risposta DELETE e PUT ?
'''

@app.route('/')
def hello_world():
  return 'Hello, World!'


@app.route('/cocktailbars', methods=['GET', 'POST'])
def cocktailbar_create_get():
  if request.method == 'GET':
    query = compose_query_CB_get(request)
    # results = engine.execute(query)
    return "query: " + query
  elif request.method == 'POST':
    J = request.get_json(force=True)
    name = J['name']
    return "voglio creare un cocktailbar", 201




@app.route('/cocktailbars/<name>', methods=['GET', 'PUT', 'DELETE'])
def cocktailbar_manage(name):
  table_name = 'cocktailbar'
  if request.method == 'GET':
    query = "SELECT * FROM " + table_name + " WHERE name = " + name
    return query, 200
  #elif request.method == 'POST':
  #  query = "NSERT INTO " + table_name + " (id, name) WHERE name = " + name
  #  return query, 200
  elif request.method == 'PUT':
    # JSON?
    query = "UPDATE " + table_name + " SET name = " + name + " WHERE name = " + name
    return query
  elif request.method == 'DELETE':
    query = "DELETE FROM " + table_name + " WHERE name = " + name
    return query


@app.route('/cocktailbars/<name>/cocktails', methods=['GET', 'POST'])
def cocktails_create_get(name):
  if request.method == 'GET':
    return "voglio ottenere un cocktail di un cocktailbar. name:" + name, 200
  elif request.method == 'POST':
    return "voglio inserire un cocktail di un cocktailbar. name:" + name, 201


@app.route('/cocktailbars/<name>/cocktails/<cocktail_name>', methods=['GET', 'PUT', 'DELETE'])
def cocktailname_manage(name, cocktail_name):
  if request.method == 'GET':
    pass
  elif request.method == 'PUT':
    pass
  elif request.method == 'DELETE':
    pass



if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port)
