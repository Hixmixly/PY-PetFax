from flask import Flask, render_template

app = Flask(__name__)

# Sample data for pets
pets = [
    {
        "id": 1,
        "name": "Bella",
        "image": "/static/alvan-nee-ZCHj_2lJP00-unsplash.jpg",
        "fun_fact": "Loves playing fetch!"
    },
    {
        "id": 2,
        "name": "Charlie",
        "image": "/static/emiliano-vittoriosi-3FSBkX4yG80-unsplash.jpg",
        "fun_fact": "Great at cuddles!"
    },
    {
        "id": 3,
        "name": "Max",
        "image": "/static/karsten-winegeart-5PVXkqt2s9k-unsplash.jpg",
        "fun_fact": "Always chasing butterflies!"
    }
]


# Root route
@app.route('/')
def index():
    return 'Hello, this is PetFax!'

# Pets index route
from flask import render_template

@app.route('/pets')
def pets_index():
    return render_template('pets/pet_index.html', pets=pets)

# Pet show page route
@app.route('/pet_show/<int:id>')
def pet_show(id):
    pet = next((pet for pet in pets if pet['id'] == id), None)
    if pet is None:
        return "Pet not found", 404
    return render_template('pets/pet_show.html', pet=pet)

# Facts create page route
@app.route('/facts/new')
def new_fact():
    return render_template('new_fact.html')

if __name__ == "__main__":
    app.run(debug=True)
