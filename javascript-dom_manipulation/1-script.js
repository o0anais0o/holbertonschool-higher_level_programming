document.querySelector('#red_header').addEventListener('click', function () {
  document.querySelector('header').style.color = '#FF0000';
});

/* 
Explications :
document.querySelector('#red_header') sélectionne l’élément avec l’id red_header.
.addEventListener('click', ...) écoute le clic sur cet élément.
Quand il y a un clic, on sélectionne la balise <header> et on change sa couleur de texte en rouge (#FF0000).

Instructions :
Ouvrir 1-main.html dans le navigateur. 
Cliquer sur le texte « Red header ». Le texte du <header> devient rouge. 
*/