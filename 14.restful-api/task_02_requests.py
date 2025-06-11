import requests
import csv


def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])
#   fetch_and_print_posts() :
# - Envoie une requête GET à l’API.
# - Affiche le code de statut (ex : 200).
# - Si la requête réussit, convertit la réponse JSON en liste Python.
# - Affiche le titre de chaque post.


def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        data = [
            {
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            }
            for post in posts
        ]
#   fetch_and_save_posts() :
# - Envoie une requête GET à l’API.
# - Si la requête réussit, extrait les champs id, title, body de chaque post.
# - Écrit ces données dans un fichier CSV nommé posts.csv
#   avec les colonnes correspondantes.
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            # csv.DictWriter : écrit une liste de dictionnaires
            #                 dans un fichier CSV.
            writer = csv.DictWriter(
                csvfile,
                fieldnames=['id', 'title', 'body']
            )
            writer.writeheader()
            writer.writerows(data)

# requests.get(url) : envoie une requête HTTP GET.
# response.status_code : vérifie le succès de la requête.
# response.json() : convertit la réponse JSON en objet Python.
