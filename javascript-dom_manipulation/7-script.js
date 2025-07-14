fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    const ul = document.querySelector('#list_movies');
    data.results.forEach(film => {
      const li = document.createElement('li');
      li.textContent = film.title;
      ul.appendChild(li);
    });
  });

/*
Explications :
On utilise fetch pour récupérer la liste des films.
On attend la réponse, puis on la convertit en JSON.
Pour chaque film dans data.results, on crée un <li> avec le titre et on l’ajoute à la liste <ul id="list_movies">.

Instructions :
Ouvrir 7-main.html dans le navigateur.
Tous les titres des films Star Wars s’afficheront dans la liste.
*/