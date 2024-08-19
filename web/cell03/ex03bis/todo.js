$(document).ready(function() {
    // Charger la liste depuis les cookies s'il existe
    loadTodoList();

    // Ajouter un nouveau to do
    $('#newTodoButton').click(function() {
        var taskName = prompt('Entrez la nouvelle t\xE2che:');
        if (taskName) {
            addTodoItem(taskName);
            saveTodoList();
        }
    });

    // Supprimer un to do au clic
    $('#ft_list').on('click', '.todo-item', function() {
        var confirmDelete = confirm('Voulez-vous vraiment supprimer cette t\xE2che ?');
        if (confirmDelete) {
            $(this).remove();
            saveTodoList();
        }
    });

    // Fonction pour ajouter un nouvel élément to do
    function addTodoItem(taskName) {
        var newItem = $('<div class="todo-item">' + taskName + '</div>');
        $('#ft_list').prepend(newItem);
    }

    // Fonction pour charger la liste depuis les cookies
    function loadTodoList() {
        var todoList = getCookie('todoList');
        if (todoList) {
            var tasks = todoList.split(',');
            tasks.forEach(function(task) {
                addTodoItem(task);
            });
        }
    }

    // Fonction pour sauvegarder la liste dans les cookies
    function saveTodoList() {
        var tasks = [];
        $('.todo-item').each(function() {
            tasks.push($(this).text());
        });
        setCookie('todoList', tasks.join(','), 7); // Cookie valide pendant 7 jours
    }

    // Fonction utilitaire pour obtenir un cookie
    function getCookie(name) {
        var cookieName = name + '=';
        var decodedCookie = decodeURIComponent(document.cookie);
        var cookieArray = decodedCookie.split(';');
        for (var i = 0; i < cookieArray.length; i++) {
            var cookie = cookieArray[i];
            while (cookie.charAt(0) === ' ') {
                cookie = cookie.substring(1);
            }
            if (cookie.indexOf(cookieName) === 0) {
                return cookie.substring(cookieName.length, cookie.length);
            }
        }
        return null;
    }

    // Fonction utilitaire pour définir un cookie
    function setCookie(name, value, days) {
        var expires = '';
        if (days) {
            var date = new Date();
            date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
            expires = '; expires=' + date.toUTCString();
        }
        document.cookie = name + '=' + encodeURIComponent(value) + expires + '; path=/';
    }
});
