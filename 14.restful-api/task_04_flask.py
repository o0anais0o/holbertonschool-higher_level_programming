from flask import Flask, jsonify, request

app = Flask(__name__)

# Stockage en mémoire des utilisateurs
users = {}

@app.route('/')  # '/' : Affiche “Welcome to the Flask API!”.
def home():
    return "Welcome to the Flask API!"

@app.route('/status')  # '/status' : Affiche “OK”.
def status():
    return "OK"

# '/data' : Retourne la liste des usernames enregistrés, au format JSON.
@app.route('/data')
def get_usernames():
    # Retourne la liste des usernames
    return jsonify(list(users.keys()))

# /users/<username> : Retourne l’objet complet de l’utilisateur si trouvé,
#                     sinon une erreur 404.
@app.route('/users/<username>')  
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


# /add_user (POST) : Ajoute un utilisateur à partir de données JSON envoyées
#                    dans la requête. Retourne une confirmation ou une erreur 
#                    si le champ username est absent.
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data or 'username' not in data:
        return jsonify({"error": "Username is required"}), 400
    username = data['username']
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }
    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201

if __name__ == "__main__":
    app.run()

# @app.route() : défini les routes (endpoints).
# jsonify() retourne des réponses JSON.
# request.get_json(). : gére les requêtes POST et lit le JSON envoyé.
