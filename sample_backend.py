from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#export FLASK_APP=sample_backend.py
#export FLASK_ENV=development

users = { 
    'users_list' :
    [
        { 
            'id' : 'xyz789',
            'name' : 'Charlie',
            'job': 'Janitor',
        },
        {
            'id' : 'abc123', 
            'name': 'Mac',
            'job': 'Bouncer',
        },
        {
            'id' : 'ppp222', 
            'name': 'Mac',
            'job': 'Professor',
        }, 
        {
            'id' : 'yat999', 
            'name': 'Dee',
            'job': 'Aspring actress',
        },
        {
            'id' : 'zap555', 
            'name': 'Dennis',
            'job': 'Bartender',
        }
    ]
}

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/users/<id>')
def get_user(id):
    if id :
        for user in users['users_list']:
            if user['id'] == id:
                return user
        return ({})
    return users

@app.route('/users', methods=['GET', 'POST', 'DELETE'])
def get_users():
    if request.method == 'GET':
        points_max = 0
        search_username = request.args.get('name')
        if search_username:
            points_max += 1
        search_job = request.args.get('job')
        if search_job:
            points_max += 1
        search_id = request.args.get('id')
        if search_id:
            points_max += 1
        subdict = {'users_list' : []}
        
        for user in users['users_list']:
            points = 0
            if search_username:
                if (search_username == user['name']):
                    points += 1
            if search_job:
                if (search_job == user['job']):
                    points += 1
            if search_id:
                if (search_id == user['id']):
                    points += 1
            if (points == points_max):
                subdict['users_list'].append(user)
        return subdict
    
    elif request.method == 'POST':
        userToAdd = request.get_json()
        users['users_list'].append(userToAdd)
        resp = jsonify(success = True)
        #resp.status_code = 200 #optionally, you can always set a response code. 
        # 200 is the default code for a normal response
        return resp
    
    elif request.method == 'DELETE':
        userToRm = request.get_data().decode("utf-8")
        subdict = {'users_list' : []}
        found = False
        print(userToRm)
        if userToRm:
            for user in reversed(users['users_list']):
                if (user['name'] == userToRm) | (user['id'] == userToRm):
                    found = True
                    try:
                        users['users_list'].remove(user)
                        subdict['users_list'].append(user)
                    except:
                        resp = jsonify(success = False)
                        resp.status_code = 404
                        return resp
        resp = jsonify(success = found, deleted_users = subdict['users_list'])
        return resp