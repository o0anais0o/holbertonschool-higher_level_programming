document.querySelector('#toggle_header').addEventListener('click', function () {
  const header = document.querySelector('header');
  if (header.classList.contains('red')) {
    header.classList.remove('red');
    header.classList.add('green');
  } else {
    header.classList.remove('green');
    header.classList.add('red');
  }
});

/* Explications :
On sélectionne le bouton avec l’id toggle_header.
Au clic, on sélectionne le <header>.
Si le header a la classe red, on la remplace par green.
Sinon (donc s’il a green), on la remplace par red.
Le header aura toujours soit la classe red soit la classe green, jamais les deux, jamais aucune.
Instructions : Ouvrir 3-main.html dans le navigateur. 
Cliquer sur « Toggle header » : la couleur du header alterne entre rouge et vert à chaque clic.*/