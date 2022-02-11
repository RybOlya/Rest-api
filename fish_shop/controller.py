from main import app, db
from flask import request
from flask import jsonify
@app.route('/')

def index():
    return "Hooray"

@app.route('/fish/<id>')
def get_fish():
    print(id)
    return "my fish is gorgeous"

@app.route('/fish', methods =["GET"])
def get_all_fishes():
    return "all fish"

@app.route('/fish', methods =["POST"])
def create_fish():

    fish = Fish( name = request.json["name"], origin = request.json["origin"])
    db.session.add(fish)

    db.session.commit()

    return jsonify(Fish.query.all())
