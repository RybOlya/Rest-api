from main import app

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
    print("fish created")