document.addEventListener('DOMContentLoaded', function() {
    var addButton = document.getElementById('addButton');
    var newMessageInput = document.getElementById('newMessage');

    if (addButton) {
        addButton.addEventListener('click', function() {
            var newMessage = newMessageInput.value;

            if (newMessage.trim() !== "") {
                fetch('/add_message/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'X-CSRFToken': getCookie('csrftoken')
                    },
                    body: 'content=' + encodeURIComponent(newMessage)
                })
                .then(response => response.json())
                .then(data => {
                    var messageList = document.getElementById('messageList');
                    var newMessageItem = document.createElement('li');
                    newMessageItem.textContent = data.content;
                    messageList.appendChild(newMessageItem);

                    // Effacer le contenu de la zone de texte après avoir ajouté le message
                    newMessageInput.value = "";
                })
                .catch(error => {
                    console.error('Erreur lors de l\'ajout du message:', error);
                });
            }
        });
    } else {
        console.error('L\'élément avec l\'ID "addButton" n\'a pas été trouvé.');
    }
});
