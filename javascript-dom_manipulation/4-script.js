document.querySelector('#add_item').addEventListener('click', function () {
  const ul = document.querySelector('.my_list');
  const li = document.createElement('li');
  li.textContent = 'Item';
  ul.appendChild(li);
});

/* 
Explications :
On sélectionne l’élément avec l’id add_item.
Lors d’un clic, on sélectionne la liste <ul class="my_list">.
On crée un nouvel élément <li>, on lui donne le texte « Item », puis on l’ajoute à la liste.

Instructions : 
Ouvrir 4-main.html dans le navigateur.
Cliquer sur « Add item » : un nouvel élément <li>Item</li> est ajouté à la liste à chaque clic.
*/