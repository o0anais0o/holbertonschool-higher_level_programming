from http.server import BaseHTTPRequestHandler, HTTPServer

# BaseHTTPRequestHandler :
# classe à hériter pour définir le comportement du serveur.
class SimpleAPIHandler(BaseHTTPRequestHandler):
    # do_GET(self) : méthode appelée pour chaque requête GET.
    def do_GET(self):
        # Réponse pour la racine /
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        # Réponse pour /data
        elif self.path == '/data':
            import json
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())
        # Réponse pour /status
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")
        # Réponse pour /info
        elif self.path == '/info':
            import json
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(info).encode())
        # Pour tout autre endpoint : 404
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print("Server running on http://localhost:8000")
    httpd.serve_forever()

# Explications du code :
# self.path : contient le chemin demandé (ex: /, /data, etc.).
# send_response() : envoie le code HTTP (200, 404...).
# send_header() : ajoute un en-tête HTTP (ex: type de contenu).
# end_headers() : termine l’envoi des en-têtes.
# wfile.write() : envoie le contenu de la réponse (texte ou JSON).
