from flask import Flask
from app import app

#app = Flask(__name__)
#@app.route('/')
#def homepage():
#    return 'Minha'

if __name__=='__main__':
    app.run(debug=True)