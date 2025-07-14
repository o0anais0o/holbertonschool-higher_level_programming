document.querySelector('#update_header').addEventListener('click', function () {
  document.querySelector('header').textContent = 'New Header!!!';
});

/*
Explications :
On sélectionne l’élément avec l’id update_header.
Lors d’un clic, on sélectionne la balise <header> et on met à jour son texte avec textContent.

Instructions :
Ouvrir 5-main.html dans le navigateur.
Clique sur « Update the header » : le texte du <header> devient New Header!!!.
*/