#!/usr/bin/python3


# Importation des modules nécessaires
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity, get_jwt
)

# Initialise l'application Flask
app = Flask(__name__)
# Crée une instance pour l'authentification basique
auth = HTTPBasicAuth()
# Définit la clé secrète pour les tokens JWT
app.config['JWT_SECRET_KEY'] = "secret-key-change-me"
# Active la gestion JWT sur l'app
jwt = JWTManager(app)

# Dictionnaire simulant une base d'utilisateurs
accounts = {
    "user1": {
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# Vérifie les identifiants pour l'auth basique
@auth.verify_password
def check_credentials(username, password):
    # Récupère les infos utilisateur
    user = accounts.get(username)
    # Vérifie si l'utilisateur existe et le mot de passe est correct
    if user and check_password_hash(user["password"], password):
        return username
    return None


# Route protégée par auth basique
@app.route("/basic-protected")
@auth.login_required
def protected_basic():
    # Renvoie un message si l'utilisateur est authentifié
    return "Basic Auth: Access Granted", 200


# Route pour se connecter et obtenir un token JWT
@app.route("/login", methods=["POST"])
def login_jwt():
    # Récupère les données envoyées en JSON
    payload = request.get_json()
    # Vérifie que le JSON contient un nom et un mot de passe
    if not payload or "username" not in payload or "password" not in payload:
        return jsonify({"error": "Missing credentials"}), 401

    # Vérifie si l'utilisateur existe
    user_record = accounts.get(payload["username"])
    # Vérifie que le mot de passe est correct
    if not user_record or not check_password_hash(user_record["password"], payload["password"]):
        return jsonify({"error": "Invalid credentials"}), 401

    # Crée un token avec l'identité et le rôle
    identity = {
        "username": payload["username"],
        "role": user_record["role"]
    }
    # Génère le token d'accès
    token = create_access_token(identity=identity)
    # Renvoie le token
    return jsonify({"access_token": token}), 200


# Route protégée par JWT
@app.route("/jwt-protected")
@jwt_required()
def secured_area():
    # Renvoie un message si le token est valide
    return "JWT Auth: Access Granted", 200


# Route accessible uniquement aux admins
@app.route("/admin-only")
@jwt_required()
def admin_zone():
    # Récupère l'identité de l'utilisateur depuis le token
    user = get_jwt_identity()
    # Vérifie si le rôle est admin
    if user.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    # Accès autorisé pour les admins
    return "Admin Access: Granted", 200


# Gestion de l'absence de token JWT
@jwt.unauthorized_loader
def token_absent(e):
    return jsonify({"error": "Missing or invalid token"}), 401


# Gestion des tokens JWT invalides
@jwt.invalid_token_loader
def token_invalid(e):
    return jsonify({"error": "Invalid token"}), 401


# Gestion des tokens JWT expirés
@jwt.expired_token_loader
def token_expired(header, data):
    return jsonify({"error": "Token has expired"}), 401


# Gestion des tokens révoqués
@jwt.revoked_token_loader
def token_revoked(header, data):
    return jsonify({"error": "Token has been revoked"}), 401


# Gestion des tokens JWT non frais
@jwt.needs_fresh_token_loader
def fresh_required(header, data):
    return jsonify({"error": "Fresh token required"}), 401


# Lance l'application Flask
if __name__ == "__main__":
    app.run()
