document.addEventListener('DOMContentLoaded', function () {
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.json())
    .then(data => {
      document.querySelector('#hello').textContent = data.hello;
    });
});

/*
Explications :
On attend que le DOM soit chargé avec DOMContentLoaded pour s’assurer que l’élément avec l’id hello existe.
On utilise fetch pour récupérer la traduction de « hello » en français.
On affiche la valeur dans l’élément avec l’id hello.

Instructions :
Ouvrir 8-main.html dans le navigateur.
Le mot « Bonjour » (ou la traduction retournée par l’API) s’affichera dans le <div id="hello"></div>.
*/