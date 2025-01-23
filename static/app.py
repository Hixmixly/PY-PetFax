# app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, this is PetFax!'

if __name__ == "__main__":
    app.run(debug=True)


# pets index route 
@app.route('/pets')
def pets ():
     return 'These are our pets available for adoption!'