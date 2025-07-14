document.querySelector('#red_header').addEventListener('click', function () {
  document.querySelector('header').classList.add('red');
});

/* Explications :
On sélectionne l’élément avec l’id red_header.
Lors d’un clic, on ajoute la classe red à la balise <header>.
La classe .red est déjà définie dans le <style> de la page pour appliquer la couleur rouge.
Instructions : Ouvrir 2-main.html dans le navigateur. Cliquer sur « Red header » : le texte du <header> devient rouge. */