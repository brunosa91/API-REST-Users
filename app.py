from flask import Flask, jsonify

user = [
    {
        'name':'Bruno Santana de Sá',
        'email':'brunosantana@gmail.com',
        'telefone':'(11)988887777'
    }
]

app =  Flask(__name__)

@app.route('/add_user', methods=['POST'])
def createUser():
    pass


@app.route('/users' , methods=['GET'])
def getUser():
    return jsonify(user)

@app.route('/users/<id>' , methods=['GET'])
def getUserById(id):
    pass

@app.route('/edit_user/<id>' , methods=['PUT'])
def editUserById(id):
    pass

@app.route('/delete_user/<id>' , methods=['DELETE'])
def deleteUserById(id):
    pass

app.run(port=5000)