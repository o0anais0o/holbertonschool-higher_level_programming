fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())
  .then(data => {
    document.querySelector('#character').textContent = data.name;
  });

/*
Explications :
On utilise fetch pour récupérer les données du personnage depuis l’URL donnée.
On convertit la réponse en JSON.
On affiche la propriété name dans l’élément ayant l’id character.

Instructions :
Ouvrir 6-main.html dans le navigateur.
Le nom du personnage (Leia Organa) s’affichera dans le <div id="character"></div>.
*/