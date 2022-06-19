from flask import Flask

app =  Flask(__name__)

@app.route('/add_user', methods=['POST'])
def createUser():
    pass


@app.route('/users' , methods=['GET'])
def getUser():
    pass

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