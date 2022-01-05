/* Dark Mode/Mode Nuit */
const darkMode = document.getElementById('dark-mode');

darkMode.addEventListener('change', () => {
  document.body.classList.toggle('dark');
});

/* Un problème ? Besoin d'aide ? */
var envoyer = document.querySelector('.envoyer');
var textbox = document.querySelector('.textbox');
var textarea = document.querySelector('#test');

envoyer.addEventListener('click', function () {
    textbox.value = '';
    textarea.value = '';
    alert("Votre message à bien était envoyé. Un administrateur va vous répondre dès que possible !");
});