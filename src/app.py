#Dependencies
from flask import Flask
from flask import request
from flask import jsonify
from markupsafe import escape


#Server Configuration
app = Flask(__name__)


activeUsers = {}

#Routing
@app.route('/')
def hello_world():
    return 'Gatto se la come'


@app.route('/update/<userID>')
def user_capture(userID):
    activeUsers[request.remote_addr] = userID
    print('UserID: ', userID ,'ip: ', request.remote_addr)

    for user in activeUsers:
        print(user)

    return 'Status'