from flask import Flask

app =  Flask(__name__)

@app.route('/')
def home():
    return "testando rota"

app.run(port=5000)